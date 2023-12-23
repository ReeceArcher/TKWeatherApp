import requests
from pprint import pprint


# This Program is used to gather weather data from the openweathermap API
# The information is then passed to Main.Py where it is outputted in the
# TKinter GUI.

# Information passed is current temperature, feels_like temperature, temp_high, temp_low, and current_condition
# Built on 12/22/23 @2030


# Function to get Weather data from given city
def get_weather_data(city):
    api_key = ""  # Replace with API key from openweathermap
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial&lang=en".format(city,
                                                                                                        api_key)  # URL provide from openweathermap website

    try:
        response = requests.get(url)  # Makes a request to the API
        data = response.json()  # Converts the data to json

        return data

    except Exception as e:
        print("Something went")  # Error handling
        return None


# Function to format and output weather data
def output_weather_data(data):
    if data:
        # Remove the int if decimal place is wanted
        # Extracts the information from the json file and convert
        # the data to an int
        location = data["name"]
        country = data["sys"]["country"]
        temperature = int(data["main"]["temp"])
        feels_like = int(data["main"]["feels_like"])
        temp_high = int(data["main"]["temp_max"])
        temp_low = int(data["main"]["temp_min"])
        current_condition = data["weather"][0]["description"]

        # Return the information formatted
        return {
            "location": location + "," + country,
            "Temperature": f"The temperature is: {temperature}°F",
            "Feels Like": f"It feels like: {feels_like}°F",
            "High": f"The high today is: {temp_high}°F",
            "Low": f"The low today is: {temp_low}°F",
            "Condition": f"The current condition is: {current_condition}"

            # Prints the information using pprint
            # to the console in a readable format

            # pprint("The temperature is: {}".format(temperature) + "°")
            # pprint("It feels like: {}".format(feels_like) + "°")
            # pprint("The high today is: {}".format(temp_high) + "°")
            # pprint("The low today is: {}".format(temp_low) + "°")
        }

    else:
        print("No data")  # Error handling
