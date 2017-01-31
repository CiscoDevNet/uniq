#!/bin/bash

# This script will trigger backup on specific cluster, wait for backup being done, and download it
# to local directory.
# In local directory, it only keep 10 latest backup files.

# How to use this script
#
# 1. Set up ssh authorization
#        a. generate rsa key pair if it's never done before. (Do not enter a passphrase)
#           command: ssh-keygen -t rsa
#        b. append public key to the remote cluster (Please replace 1.1.1.1 with correct ip)
#           command: cat ~/.ssh/id_rsa.pub | ssh grapevine@1.1.1.1 'cat >> .ssh/authorized_keys'
#        c. make sure keychain is installed on current server.
#           For ubuntu: sudo apt-get install keychain
#           For mac: brew install keychain
#
# 2. Provide cluster's credentials.
#       Modefies variables 'host', 'port', 'username', 'password', 'ssh_username',
#       'path_to_store_backup' with valid value.
#
# 3. Set up schedule and logging, using cron.
#       command: crontab -e
#       edit it with vi, modify and paste following command:
#       0 0,12 * * * . /path/to/retrieve_backup.sh >> /path/to/log/retrieve_backup.log 2>&1


HOME=/home/username                             # Your home directory

host="1.1.1.1"                                  # Cluster's address
port="14141"                                    # Cluster's management site's port number
username="admin"                                # Username to login to APIC-EM
password="password"                             # Password to login to APIC-EM
ssh_username="admin"                            # Username to login to grapevine server
path_to_store_backup="$HOME/backup"             # Directory to save backup files
                                                # Please ONLY put backup files to this folder

# DO NOT MODIFY THESE VARIABLES
PATH=/bin:/usr/bin:/sbin:/usr/local/bin
FILE_DIR="/srv/grapevine/replicated-storage/backups/"
token=""

# Logging in to cluster
echo "[`date`] Logging to $host and getting token."
response=$(curl -k -sS -H "Content-Type: application/json" -X POST \
    -d "{\"username\":\"$username\",\"password\":\"$password\"}" https://$host:$port/api/auth/login)

token=$(echo $response | python -c "from __future__ import print_function; \
    import sys, json; print(json.load(sys.stdin)['response']['token'])")

# Retrieve token
if [ ! -z $token ]; then
    echo "[`date`] Got token successfully"
else
    echo "[`date`] Fail to get token, please check the connection and credential."
    exit 1
fi

# Trigger backup
echo "[`date`] Triggering backup."

response=$(curl -k -sS -H "Content-Type: application/json" -H "token: $token" -X POST \
    https://$host:$port/api/backup)
task_id=$(echo $response | python -c "from __future__ import print_function; import sys, json; \
    print(json.load(sys.stdin)['response']['task_id'])")

echo "[`date`] Task id of backup is $task_id"


check_status() {
    response=$(curl -k -sS -H "Content-Type: application/json" -H "token: $token" -X GET \
        https://$host:$port/api/backup/info/$task_id)
    status=$(echo $response | python -c "from __future__ import print_function; import sys, json; \
        print(json.load(sys.stdin)['response']['status'])")
    echo $status
}

echo "[`date`] Waiting for task complete"
sleep 30

# Wait for backing up complete
while [ "$(check_status)" != "success" ]; do
    if [ "$(check_status)" == "in_progress" ]; then
        echo "[`date`] Status of backup is in_progress. Wait 10 seconds."
        sleep 10
    else
        echo "[`date`] Status is not 'success' or 'in_progress'. Task failed."
        exit 1
    fi
done

echo "[`date`] Backup succeeded."

# Get the backup file name
response=$(curl -k -sS -H "Content-Type: application/json" -H "token: $token" -X GET \
    https://$host:$port/api/backup/info/$task_id)
filename=$(echo $response | python -c "from __future__ import print_function; import sys, json; \
    print(json.load(sys.stdin)['response']['filename'])")

echo "[`date`] File name of the back up file is $filename"

filepath="$FILE_DIR$task_id/$filename"
echo "[`date`] Backup file locates in $filepath"

echo "[`date`] Downloading backup file and save as $path_to_store_backup/$filename."

if [ ! -d "$path_to_store_backup" ]; then
    mkdir $path_to_store_backup
fi

eval `keychain -q --noask --eval id_rsa`
scp -i $HOME/.ssh/id_rsa $ssh_username@$host:$filepath $path_to_store_backup

if [ $? -eq 0 ]; then
    echo "[`date`] Downloaded successfully."
else
    echo "[`date`] Failed to download backup file."
    exit 1
fi

# Only keep 10 latest backup and delete all old backups.
ls -1t $path_to_store_backup | tail -n +11 | xargs -I % sh -c \
    'echo "[`date`] Deleting out of date backup: %";rm -f %;'
