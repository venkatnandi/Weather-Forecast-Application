import requests
import json

def get_weather(api_key, location):
    # Define the API endpoint
    endpoint = "https://api.openweathermap.org/data/2.5/weather"

    # Set the parameters for the API request
    params = {
        "q": location,          # Location (e.g., city name)
        "appid": api_key,       # Your API key
        "units": "metric"      # Units for temperature (e.g., Celsius)
    }

    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            try:
                # Attempt to parse the JSON response
                weather_data = response.json()
                return weather_data
            except json.JSONDecodeError:
                print("Error: Unable to decode JSON data from the API response.")
                return None
        else:
            print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to the API. {str(e)}")
        return None

# Replace with your OpenWeatherMap API key u have to mention your own api key of your area
api_key = "0991c061d60f255eb77d91ca016c9e23"

# Specify the location for which you want to fetch weather data
location = input("Enter a location: ")  # Replace with your desired location

# Get weather data for the specified location
weather_data = get_weather(api_key, location)

# Display the weather data
if weather_data:
    print(f"Weather in {location}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Description: {weather_data['weather'][0]['description']}")
