import requests 
import requests.auth
import json
import estimates

LYFT_CLIENT_ID = 'a83m8aY1GflS'
LYFT_CLIENT_SECRET = 'SANDBOX-NqGnOBR6IybCJ5_wgopl2rYSXlaYroVU'

# def get_sandbox():

# 	access_token = estimates.get_access_token()
	
#     headers = {"Authorization": "bearer " + access_token}
#     url = "https://api.lyft.com/v1/sandbox/rides/{ride_id}".format(ride_id="4319057680757320826")

#     post_data = {"Content-Type": "application/json",
#              "status": "accepted"}

#     response = requests.get(url, headers=headers, data=post_data)

#     result = response.json()["eta_estimates"]
    
#     return eta

def get_public_token():

    client_auth = requests.auth.HTTPBasicAuth(LYFT_CLIENT_ID, LYFT_CLIENT_SECRET)
    post_data = {
        'grant_type': 'client_credentials',
        'scope': 'public'
    }
    return requests.post('https://api.lyft.com/oauth/token', auth=client_auth, data=post_data)

def get_access():

	access_info = requests.get('https://api.lyft.com/oauth/authorize', params={
        'client_id': LYFT_CLIENT_ID,
        'response_type': 'code',
        'scope': 'public rides.read rides.request',
        'state': 'payload'
    })

	print(access_info.url)


def get_user_token(authorization_code):

    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {
        'grant_type': 'authorization_code',
        'code': authorization_code
    }
    return requests.post('https://api.lyft.com/oauth/token', auth=client_auth, data=post_data)

def get_cost(token, pickup_location, destination):

    return requests.get('https://api.lyft.com/v1/cost', headers={
        'Authorization': 'Bearer ' + token.json()['access_token']
    }, params={
        'start_lat': pickup_location.json()['locations'][0]['feature']['geometry']['y'],
        'start_lng': pickup_location.json()['locations'][0]['feature']['geometry']['x'],
        'end_lat': destination.json()['locations'][0]['feature']['geometry']['y'],
        'end_lng': destination.json()['locations'][0]['feature']['geometry']['x']
    })

def get_ride(origin, destination, ride_type):
    parameters = {
        'ride_type': ride_type,
        'origin': origin,
        'destination': destination,
    }

    print("READY TO CALL API")

    ride = requests.post('https://api.lyft.com/v1/rides', headers={
        'Authorization': 'Bearer ' + estimates.get_access_token(),
        'Content-Type': 'application/json'
    }, data=json.dumps(parameters))

    print("READY TO RETURN INFO")
    ride_info = ride.json()
    print(ride_info)
    # print(str(ride_info['state']))

    return ride_info

def build_location(lat, lng):

	new_dict = {
        'lat': lat,
        'lng': lng,
    }

	return new_dict

def request_ride(orig_lat, orig_lng, dest_lat, dest_lng, num_friends):

	print("GETTING ACCESS")

	get_access()

	origin = build_location(orig_lat, orig_lng)
	destination = build_location(dest_lat, dest_lng)

	if num_friends <= 1:
		ride_type = "Lyft Line"
	elif num_friends <= 3:
		ride_type = "Lyft"
	else:
		ride_type = "Lyft Plus"

	print("READY TO GET RIDE INFO")

	request_info = get_ride(origin, destination, ride_type)

	print("INFO HAS BEEN RETURNED")

	return request_info


