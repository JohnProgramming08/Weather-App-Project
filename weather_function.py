import datetime as dt
import requests

def get_weather(app):
    # Connect to the API
    try:
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        api_key = "f35a67974062073a04ab60d09446e6e6"
        city = app.weather_page.city_entry.get()

        url = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(url).json()
    
    except:
        app.show_error("City not found")

    def celsius(kelvin):
        return round(kelvin - 273.15)

    # Declare all the variables for weather information
    temperature = celsius(response["main"]["temp"])
    feels_like = celsius(response["main"]["feels_like"])
    wind_speed = response["wind"]["speed"]
    humidity = response["main"]["humidity"]
    description = response["weather"][0]["description"]
    sunrise_time = dt.datetime.fromtimestamp(response["sys"]["sunrise"])
    sunset_time = dt.datetime.fromtimestamp(response["sys"]["sunset"])

    # Display weather information
    app.weather_page.temp_label.configure(text=f"Temperature: {temperature}°C")
    app.weather_page.feels_like_label.configure(text=f"Feels Like: {feels_like}°C")
    app.weather_page.wind_speed_label.configure(text=f"Wind Speed: {wind_speed} m/s")
    app.weather_page.humidity_label.configure(text=f"Humidity: {humidity}%")
    app.weather_page.current_weather.configure(text=f"Current Weather: {description}")
    app.weather_page.sunset_time.configure(text=f"Sunset Time: {sunset_time}")
    app.weather_page.sunrise_time.configure(text=f"Sunrise Time: {sunrise_time}")

    def display_recommendations(app, hat, umbrella, coat, sunscreen):
        app.weather_page.hat_recommendation.configure(text=f"Hat: {hat}")
        app.weather_page.umbrella_recommendation.configure(text=f"Umbrella: {umbrella}")
        app.weather_page.coat_recommendation.configure(text=f"Coat: {coat}")
        app.weather_page.sunscreen_recommendation.configure(text=f"Sunscreen: {sunscreen}")

    # Create and display recommendations
    hat = "No Recommendation"
    umbrella = "No Recommendation"
    coat = "No Recommendation"
    sunscreen = "No Recommendation"
    if temperature > 20:
        sunscreen = "Yes"

    if humidity < 50:
        coat = "Yes"

    if description == "clear sky":
        hat = "Yes"

    if description == "shower rain":
        umbrella = "Yes"
        coat = "Yes"

    if description == "rain":
        umbrella = "Yes"
        coat = "Yes"

    if description == "thunderstorm":
        umbrella = "Yes"
        coat = "Yes"

    if description == "snow":
        umbrella = "Yes"
        coat = "Yes"

    display_recommendations(app, hat, umbrella, coat, sunscreen)
  