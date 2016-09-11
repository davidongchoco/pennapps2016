
import requests 
import requests.auth
import json

LYFT_CLIENT_ID = 'a83m8aY1GflS'
LYFT_CLIENT_SECRET = 'SANDBOX-NqGnOBR6IybCJ5_wgopl2rYSXlaYroVU'

latitude = 37.7833
longitude = -122.4167

def get_access_token():

    client_auth = requests.auth.HTTPBasicAuth(LYFT_CLIENT_ID, LYFT_CLIENT_SECRET)
    post_data = {"Content-Type": "application/json",
                 "grant_type": "client_credentials",
                 "scope": "public"}

    response = requests.post("https://api.lyft.com/oauth/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    access_token = token_json["access_token"]
    
    return access_token

def get_ride_type():

    num_friends = 2

    if num_friends <= 1:
        ride_type = "Lyft Line"
    elif num_friends <= 3:
        ride_type = "Lyft"
    else:
        ride_type = "Lyft Plus"

    return ride_type

def get_response():

    access_token = get_access_token()

    ride = get_ride_type()

    if ride == "Lyft Line":
        ride_type = "lyft_line"
    elif ride == "Lyft":
        ride_type = "lyft"
    else:
        ride_type = "lyft_plus"

    headers = {"Authorization": "bearer " + access_token}
    url = "https://api.lyft.com/v1/eta?lat={lat}&lng={lng}&ride_type={rt}".format(lat=latitude, lng=longitude, rt=ride_type)

    response = requests.get(url, headers=headers)

    return response


def get_eta():

    response = get_response()

    # print(response)
    eta_estimates = response.json()["eta_estimates"]
    print(eta_estimates)
    eta = eta_estimates[0]["eta_seconds"]

    eta_min = eta/60
    
    return eta_min


def get_location():

    new_dict = {
        'lat': latitude,
        'lng': longitude,
    }

    return new_dict

def set_eta(mylat, mylng):

    global latitude
    latitude = mylat

    global longitude
    longitude = mylng

    print(latitude)
    print(longitude)