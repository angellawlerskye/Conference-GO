import requests

import json

from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_location_photo_url(city, state):
    headers = {"Authorization": PEXELS_API_KEY}
    url = "https://api.pexels.com/v1/search?query=${city},${state}&per_page=1"
    params = {
        "per_page": 1,
        "query": city + " " + state,
    }
    response = requests.get(url, params=params, headers=headers)
    content = json.loads(response.content)

    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except (KeyError, IndexError):
        return {"picture_url": "No Photo Available"}


def get_weather_data(city, state):
    url = "http://api.openweathermap.org/data/2.5/weather"
    location = city + "," + state + ",US"
    params = {
        "q": location,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    response = requests.get(url, params=params)
    content = json.loads(response.content)
    return {
        "weather": {
            "temperature": content["main"]["temp"],
            "weather": content["weather"][0]["description"],
        }
    }
