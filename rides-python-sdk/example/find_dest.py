from random import randint
import rauth
import time
import yelp
import requests
import os

def get_results(start_lat,start_lng, price, rad):

    resp = requests.post('https://api.yelp.com/oauth2/token',
                         data={'grant_type': 'client_credentials',
                               'client_id': 'T6V81F2O5GgfcANv12kRdA',
                               'client_secret': 'Gj0dTHO7d9wQh4OfQmHRgbGseQjRlOn17yZW6hZ2qKJtyZfxeNz3SkkuqhuSii4M'})

    yelp_access_token = resp.json()['access_token']

    yelp_search_url = ('https://api.yelp.com/v3/businesses/search?'
        'latitude=%s&longitude=%s&sort_by=rating&'
        'price=%s&open_now_filter=True&categories=%s&radius=%i')
    results = requests.get(
        yelp_search_url % (start_lat, start_lng, price, "food,restaurants", rad),
        headers={ 'Authorization': 'Bearer %s' % yelp_access_token })

    results = results.json()['businesses']
    output = []
    for b in results:
        to_add = {}
        to_add['name'] = b['name']
        to_add['coordinates'] = b['coordinates']
        to_add['rating'] = b['rating']
        to_add['price'] = b['price']
        output.append(to_add)
    return output

print(get_results(40.8075, -73.9626, 1, 4000))