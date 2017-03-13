import requests
import json
from django.conf import settings


def request_directions(lat, lng):
    base_url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {
        'destination': '{0},{1}'.format(lat, lng),
        'origin': '{0},{1}'.format(settings.OFFICE_LATITUDE, settings.OFFICE_LONGITUDE),
        'key': settings.GEOPOSITION_GOOGLE_MAPS_API_KEY,
        'mode': 'walking'
    }
    req = requests.get(base_url, params=params)
    if req.ok:
        return req
    else:
        return None


def get_walking_time(position):
    lat = position.latitude
    lng = position.longitude

    directions = request_directions(lat, lng)
    if directions:
        data = directions.json()
        best_route = data['routes'][0]
        return sum([i['duration']['value'] for i in best_route['legs']])
    else:
        return 60000


