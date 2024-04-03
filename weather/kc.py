import requests

def get_weather_data(city, api_key):
    try:
       
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        
        
        response = requests.get(url)
        
        
        if response.status_code == 200:
            
            weather_data = response.json()
            print(weather_data) 
           
            temperature = weather_data['current']['temp_c']
            wind_direction = weather_data['current']['wind_dir']
            humidity = weather_data['current']['humidity']
            
            
            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Wind Direction: {wind_direction}")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Failed to retrieve weather data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


city_name = "thanjavur"
api_key = "475f71268bfe4af89fd65418242803"


get_weather_data(city_name, api_key)
