import requests
def Get_weather(city):
    get_weather('cdcf219c9ccb4154a3e45759252305', city)
    
def get_weather(api_key, location):
    url = 'https://api.weatherapi.com/v1/current.json'
    params = {
        'key': api_key,
        'q': location,
        'aqi': 'no'
    }
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        location_info = data['location']
        current_weather = data['current']
        print(f"Weather in {location_info['name']}, {location_info['region']}:")
        print(f"Temperature: {current_weather['temp_c']}°C")
        print(f"Condition: {current_weather['condition']['text']}")
        print(f"Humidity: {current_weather['humidity']}%")
        print(f"Wind Speed: {current_weather['wind_kph']} km/h")
    else:
        print(f"Error {response.status_code}: {data.get('error', {}).get('message', 'Unknown error')}")

city=input("Enter city name: ")
Get_weather(city)


