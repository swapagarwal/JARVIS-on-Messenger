import requests
import json

# Replace with your AQICN API key
API_KEY = "YOUR_API_KEY"

def get_aqi_for_location(location_name):
    base_url = "http://api.waqi.info/feed/"
    location_name = location_name.replace(" ", "%20")
    endpoint = f"{base_url}{location_name}/?token={API_KEY}"

    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        if data.get("status") == "ok":
            aqi = data["data"]["aqi"]
            print(f"AQI for {location_name}: {aqi}")
        else:
            print(f"Unable to retrieve AQI data for {location_name}.")
    else:
        print("Error: Unable to connect to the AQICN API.")

if __name__ == "__main__":
    location_name = input("Enter the location name (e.g., city, country): ")
    get_aqi_for_location(location_name)
Make sure you've installed the requests library using pip install requests if you haven't already. Replace "YOUR_API_KEY" with your actual API key, and you can enter a location name when prompted. The program will make a request to the API, retrieve the AQI data, and display it.

Keep in mind that different AQI sources may have different APIs and endpoints, so the above code is specific to the AQICN API. You may need to adjust the code for a different source.





