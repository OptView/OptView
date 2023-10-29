# Write on API based on the reading of the Arduino Data API

import requests
import json

# ThingSpeak API settings for reading
READ_API_BASE_URL = "https://api.thingspeak.com/channels/2316311/feeds.json"
READ_API_KEY = os.getenv('READ_API_KEY')  # Get API key from environment variable


# ThingSpeak API settings for writing
WRITE_API_BASE_URL = "https://api.thingspeak.com/update"
WRITE_API_KEY = os.getenv('WRITE_API_KEY')  # Get API key from environment variable

# Testing threshold for turning On/Off
TEMPERATURE_THRESHOLD = 20  # Example threshold

def get_last_temperature():
    params = {
        "api_key": READ_API_KEY,
        "results": 1
    }
    response = requests.get(READ_API_BASE_URL, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        feeds = data.get('feeds', [])
        if feeds:
            last_feed = feeds[0]
            temperature = float(last_feed.get('field1', 0))
            return temperature
    return None


def set_state(on):
    value = "1" if on else "0"
    params = {
        "api_key": WRITE_API_KEY,
        "field1": value
    }
    response = requests.get(WRITE_API_BASE_URL, params=params)
    print(f"Response Text: {response.text}")  # Print response text for debugging
    if response.status_code == 200:
        print(f"Successfully set state to {'On' if on else 'Off'}.")
    else:
        print(f"Failed to set state. Status code: {response.status_code}")


# Get the last temperature reading
temperature = get_last_temperature()

if temperature is not None:
    print(f"Last temperature reading: {temperature}°C")

    # Analyze the temperature and set the state
    if temperature > TEMPERATURE_THRESHOLD:
        print("Temperature exceeds threshold. Turning On.")
        set_state(True)
    else:
        print("Temperature is below threshold. Turning Off.")
        set_state(False)
else:
    print("Failed to retrieve temperature data.")

# For the PDLC Glass:
# pdlc_tint = 1 if uv_light < 90 else 0            # PDLC Glass Tinting
