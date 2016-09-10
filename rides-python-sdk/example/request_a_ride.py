from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    from urllib.parse import parse_qs
    from urllib.parse import urlparse
except ImportError:
    from urlparse import parse_qs
    from urlparse import urlparse

from builtins import input
from yaml import safe_load

from example.utils import create_uber_client
from example.utils import fail_print
from example.utils import paragraph_print
from example.utils import response_print
from example.utils import success_print

from uber_rides.client import SurgeError
from uber_rides.errors import ClientError
from uber_rides.errors import ServerError

from find_dest import get_results

# Example
# START_LAT = 37.77
# START_LNG = -122.41
# END_LAT=37.79
# END_LNG=-122.41

# New York
START_LAT = 40.8075
START_LNG = -73.9626

RESTAURANT = get_results(START_LAT, START_LNG, 2000)
END_LAT = RESTAURANT['latitude']
END_LNG = RESTAURANT['longitude']

def import_oauth2_credentials(filename='rides-python-sdk/example/oauth2_session_store.yaml'):

    with open(filename, 'r') as storage_file:
        storage = safe_load(storage_file)

    client_secret = storage.get('client_secret')
    redirect_url = storage.get('redirect_url')
    refresh_token = storage.get('refresh_token')

    credentials = {
        'access_token': storage['access_token'],
        'client_id': storage['client_id'],
        'client_secret': client_secret,
        'expires_in_seconds': storage['expires_in_seconds'],
        'grant_type': storage['grant_type'],
        'redirect_url': redirect_url,
        'refresh_token': refresh_token,
        'scopes': storage['scopes'],
    }

    return credentials

def get_ride_details():

	credentials = import_oauth2_credentials()
	api_client = create_uber_client(credentials)

	ride_details = request_ride(api_client)

	return ride_details

def get_time_estimate():
	
	credentials = import_oauth2_credentials()
	api_client = create_uber_client(credentials)

	estimate = estimate_ride(api_client)
	ride_details = request_ride(api_client)

	time = estimate_ride(api_client)

	return time

def estimate_ride(api_client):

	response = api_client.get_products(START_LAT, START_LNG)
	products = response.json.get('products')
	product_id = products[0].get('product_id')

	estimate = api_client.estimate_ride(
        product_id=product_id,
        start_latitude=START_LAT,
        start_longitude=START_LNG,
        end_latitude=END_LAT,
        end_longitude=END_LNG,
        )

	trip = estimate.json.get('trip')
	duration_estimate = trip.get('duration_estimate')

	minutes = int(duration_estimate / 60)
	return str(minutes)

def request_ride(api_client):

	response = api_client.get_products(START_LAT, START_LNG)
	products = response.json.get('products')
	product_id = products[0].get('product_id')

	response = api_client.request_ride(
    product_id=product_id,
    start_latitude=START_LAT,
    start_longitude=START_LNG,
    end_latitude=END_LAT,
    end_longitude=END_LNG,
	)

	ride_details = response.json
	str_ride_details = str(ride_details)

	return str_ride_details