import login


client = login.login()
# NorthBound API call to get all users
user_list_result = client.user.getUsers()

# Serialize the model object to a python dictionary
users = client.serialize(user_list_result)

print(users)