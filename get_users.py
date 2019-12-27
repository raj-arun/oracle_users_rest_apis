import requests
import json
from requests.auth import HTTPBasicAuth

#set the url
#make sure to replace <servername> with the correct value
url = "https://<servername>.fa.us2.oraclecloud.com/hcmRestApi/scim/Users"

#set headers
headers = {'Content-Type': "application/json",}

#invoke the REST API
#make sure to give the correct username and password
response = requests.request("GET", url,  headers=headers,auth=HTTPBasicAuth('araj', 'itsapassword'))
users = response.json()

print("List of users : \n")

# Loop through the response and print the details
for user in users["Resources"]:
    print("User Name : {}".format(user["userName"]))
    print("Display Name : {}".format(user["displayName"]))
    print("Active : {}\n".format(user["active"]))