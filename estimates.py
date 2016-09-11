
import requests 
import requests.auth
import json

LYFT_CLIENT_ID = 'a83m8aY1GflS'
LYFT_CLIENT_SECRET = 'NqGnOBR6IybCJ5_wgopl2rYSXlaYroVU'

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

def get_eta():

    access_token = get_access_token()

    headers = {"Authorization": "bearer " + access_token}
    url = "https://api.lyft.com/v1/eta?lat={lat}&lng={lng}".format(lat=latitude, lng=longitude)

    response = requests.get(url, headers=headers)

    eta_estimates = response.json()["eta_estimates"]
    print(eta_estimates)
    eta = eta_estimates[0]["eta_seconds"]
    
    return eta

def set_eta(mylat, mylng):

    global latitude
    latitude = mylat

    global longitude
    longitude = mylng

    print(latitude)
    print(longitude)