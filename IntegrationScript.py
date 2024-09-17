import requests

app_url = "https://hr-system-api/employees/new"
sailpoint_api_url = "https://sailpoint-server-url/api/v2/users"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

# Fetch new hires from HR system
app_response = requests.get(app_url)
new_employees = app_response.json()

# Provision new employees in SailPoint
for employee in new_employees:
    provision_data = {
        "name": employee['name'],
        "email": employee['email'],
        "department": employee['department'],
        "role": "BasicUser"
    }
    response = requests.post(sailpoint_api_url, headers=headers, json=provision_data)
    print(f"Provisioned: {response.json()['name']}")