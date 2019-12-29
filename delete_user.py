import requests
from requests.auth import HTTPBasicAuth


## REST API End Point URL. Make sure to give the correct server name
## User Id of the user from Oracle Cloud to be deleted
url = "https://<servername>.fa.us2.oraclecloud.com/hcmRestApi/scim/Users/88AE8D4EA2E5A561E0502E0C86CD7DDD"

## Request Header
headers = {'Content-Type': "application/json",}

## Invoke the REST API. We are using DELETE method
## Make sure to provide the correct user name and password.
response = requests.request("DELETE", url, headers=headers,auth=HTTPBasicAuth('araj', 'Itsapassword'))

## Print the response
print(response.text)