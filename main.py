import requests


def get_weather_data(apikey,city):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    try:
        data = requests.get(api_url)
        data_json = data.json()
        return data_json
    except requests.exceptions.RequestException as e:
        print(f"error{e}")
        
   
if __name__ == "__main__":
  
    api_key = input("Enter your OpenWeatherMap API key: ")
    city_name = input("Enter the city name: ")

    weather_data = get_weather_data(api_key, city_name)
    try:
        if weather_data:
            # Extract and format relevant weather information
            current_weather = weather_data["main"]
            print("Current weather in", weather_data["name"] + ":")
            print(f"- Temperature: {current_weather['temp']:.2f}°C")
            print(f"- Feels like: {current_weather['feels_like']:.2f}°C")
            print(f"- Humidity: {current_weather['humidity']}%")
            print(f"- Description: {weather_data['weather'][0]['description'].capitalize()}")  # Capitalize description

        # Access and output other data points as needed (e.g., wind speed, visibility)
        else:
            print("Could not retrieve weather data. Please check your API key and city name.")

    except Exception as e:
        print(f"error-> {e}")







