# Read the Arduino Data API
import requests

base_url = "https://api.thingspeak.com/channels/2316311/feeds.json"
api_key = "UPFQIULFL2PWXLDC"
params = {
    "api_key": api_key,
    "results": 1
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()

    # Getting the last entry if the "results" is more than 1
    last_entry = data['feeds'][-1]

    # Extracting field names
    field_names = {f"field{i}": data['channel'][f'field{i}'] for i in range(1, 8)}
    print("Field Names:")
    print(field_names)

    # Extracting field values of the last entry
    print("\nField Values for the last entry:")
    field_values = {f"field{i}": last_entry[f'field{i}'] for i in range(1, 8)}
    print(field_values)

    # Printing the entry_id of the last entry
    print("\nEntry ID of the last entry:")
    print(last_entry['entry_id'])
else:
    print(f"Failed to retrieve data: {response.status_code}")
