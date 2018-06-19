import datetime
import requests
from timezonefinder import TimezoneFinder

# The method used is similar to the one used in this post.
# https://medium.com/@cpenarrieta/one-way-to-get-the-user-current-time-from-your-alexa-skill-88b6d2b1aecf
def getTimezone(postalcode, countrycode):
    
    # Here I have used Google's Geocoding API to get the latitiute and longitude details 
    # You can learn more about it on
    # https://console.developers.google.com/apis/library/geocoding-backend.googleapis.com/?filter=category:maps&id=42fea2de-420b-4bd7-bd89-225be3b8b7b0&project=fir-demo-35581&folder&organizationId
    
    apiAccessKey = 'your-api-access-key'  # specific to user

    res = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0},{1}&key={2}'
                       .format(countryCode, zipCode, apiAccessKey)).json()

    lat = res['results'][0]['geometry']['location']['lat']
    lng = res['results'][0]['geometry']['location']['lng']
    
    # To get timezone from latitude and longitudes, Google's Time Zone API has been used.
    # https://console.developers.google.com/google/maps-apis/apis/timezone-backend.googleapis.com/metrics?folder=&organizationId=&project=fir-demo-35581&duration=PT1H
    res = requests.get('https://maps.googleapis.com/maps/api/timezone/json?location={0},{1}&timestamp={2}&key={3}'
                   .format(lat, lng, datetime.datetime.timestamp(datetime.datetime.now()),apiAccessKey)).json()

    timezone = res['timeZoneId']

    '''
    # Another way to get the timezone from latitude and longitudes is the TimezoneFinder library
    # Check the documentation on: https://pypi.org/project/timezonefinder/

    timezone = TimezoneFinder().timezone_at(lng=lng, lat=lat)
    '''
    
    return timezone

    '''
    result from first request:

    {
        'results': [{'address_components': [{'long_name': '60001',
         'short_name': '60001',
         'types': ['postal_code']},
        {'long_name': 'Alden',
         'short_name': 'Alden',
         'types': ['locality', 'political']},
        {'long_name': 'Chemung Township',
         'short_name': 'Chemung Township',
         'types': ['administrative_area_level_3', 'political']},
        {'long_name': 'McHenry County',
         'short_name': 'McHenry County',
         'types': ['administrative_area_level_2', 'political']},
        {'long_name': 'Illinois',
         'short_name': 'IL',
         'types': ['administrative_area_level_1', 'political']},
        {'long_name': 'United States',
         'short_name': 'US',
         'types': ['country', 'political']}],
       'formatted_address': 'Alden, IL 60001, USA',
       'geometry': {'location': {'lat': 42.4211019, 'lng': -88.61625889999999},
        'location_type': 'APPROXIMATE',
        'viewport': {'northeast': {'lat': 42.42245088029149,
          'lng': -88.61490991970848},
         'southwest': {'lat': 42.4197529197085, 'lng': -88.6176078802915}}},
       'place_id': 'ChIJycX2s9RdD4gRl4B2PokFhWo',
       'types': ['postal_code']}],
        'status': 'OK'
    }

    result from second request:

    {
        'dstOffset': 3600,
        'rawOffset': -21600,
        'status': 'OK',
        'timeZoneId': 'America/Chicago',
        'timeZoneName': 'Central Daylight Time'
    }

    '''