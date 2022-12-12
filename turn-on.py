# Import the necessary modules
import requests
import json

# Insert credentials here
host = ''
username = ''
password = ''

# Set the base URL for the iLO4 interface
base_url = 'https://' + host + '/redfish/v1/'
login_url = base_url + 'SessionService/Sessions'
power_url = base_url + 'Systems/1/Actions/ComputerSystem.Reset'

# Set the payload for the login request
login_payload = {'UserName': username, 'Password': password}

# Send the login request to the iLO4 interface
response = requests.post(login_url, json=login_payload, verify=False)

# Set the session key for the iLO4 interface
session_key = response.headers['X-Auth-Token']

# Use the session key to send a request to the iLO4 interface
response = requests.get(base_url, headers={'X-Auth-Token': session_key}, verify=False)

# Set the payload for the Power On request
power_on_payload = {'ResetType': 'On'}

# Send the Power On request to the iLO4 interface
response = requests.post(power_url, headers={'X-Auth-Token': session_key}, json=power_on_payload, verify=False)

# Print the response status code
print(response.status_code)

# Print the response content
print(json.loads(response.text))
