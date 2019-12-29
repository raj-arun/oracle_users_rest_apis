import requests
from requests.auth import HTTPBasicAuth


## REST API End Point URL. Make sure to give the correct server name
## User Id of the user from Oracle Cloud
url = "https://<servername>.fa.us2.oraclecloud.com/hcmRestApi/scim/Users/88AE8D4EA2E5A561E0502E0C86CD7DDD"

## Payload. We are updating the Email ID
payload = """{
			"schemas":["urn:scim:schemas:core:2.0:User"],
			"active":true,
			"emails":[{"primary":true,"value":"arunraj@quest4apps.com","type":"W"}]
            }"""

## Request Header
headers = {'Content-Type': "application/json",}

## Invoke the REST API. We are using PATCH method
## Make sure to provide the correct user name and password.
response = requests.request("PATCH", url, data=payload, headers=headers,auth=HTTPBasicAuth('araj', 'Itsapassword'))

## Print the response
print(response.text)