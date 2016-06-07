import csv

import login


def result_write_to_csv(devices_info_list):
    """ Write network devices information to csv format.

    Args:
        devices_info_list (list[NetworkDeviceDTO]): Lists of network device info instances.
    """

    f = csv.writer(open("network_devices.csv", "w+"))
    f.writerow(["Device Name", "IP Address", "MAC Address", "IOS/Firmware", "Platform",
                "Serial Number", "Devcie Role", "Device Family"])
    for device_info in devices_info_list:
        f.writerow([device_info.hostname,
                    device_info.managementIpAddress,
                    device_info.macAddress,
                    device_info.softwareVersion,
                    device_info.platformId,
                    device_info.serialNumber,
                    device_info.role,
                    device_info.family])

client = login.login()
response = client.networkdevice.getNetworkDeviceCount()
network_device_count = response.response

if not network_device_count:
    print("No device was found.")
    exit(1)
else:
    print("Found {} network devices".format(network_device_count))


# Gathering network device information
print("Gathering network device information.")
response = client.networkdevice.getAllNetworkDevice()

# Convert information and write to CSV
print("Writing network device information to csv format.")
result_write_to_csv(response.response)
print("Output stored in 'network_devices.csv' in the current working directory.")
