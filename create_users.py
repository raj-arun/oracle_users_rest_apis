import requests
from requests.auth import HTTPBasicAuth

#set the url
#make sure to replace <servername> with the correct value
url = "https://<servername>.fa.us2.oraclecloud.com/hcmRestApi/scim/Users"

#set the payload
payload = """{
			"schemas":["urn:scim:schemas:core:2.0:User"],
			"name":{"familyName":"Raj",
					"givenName":"Arun"
				    },
			"active":true,
			"userName":"araj@quest4apps.com",
			"emails":[{"primary":true,"value":"araj@quest4apps.com","type":"W"}],
			"displayName":"Arun Raj",
            "password":"Welcome@123"
            }"""

#set the headers
headers = {'Content-Type': "application/json",}

#invoke the REST API
#make sure to give the correct username and password
response = requests.request("POST", url, data=payload, headers=headers,auth=HTTPBasicAuth('araj', 'itsapassword'))

#print the response
print(response.text)