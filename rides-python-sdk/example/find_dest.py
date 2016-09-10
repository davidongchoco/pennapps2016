from random import randint
import rauth
import time


def get_results_from_params(params):

    #Obtain these from Yelp's manage access page
    consumer_key="3IzXqKWFoPm2ZnOtfpG1yA"
    consumer_secret="VslZ8Xem6kiwAYhm-0_89I6PYjk"
    token="2PbRTKDOoBp4wkqel8R2VcO048P5Ol34"
    token_secret="9VrRMdju-aok7yIMRKiIalO_mSw"
    
    session = rauth.OAuth1Session(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = token,
        access_token_secret = token_secret)
        
    request = session.get("http://api.yelp.com/v2/search",params=params)

    r = randint(0,19)
    # return request[r].location.coordinate
    rest = request.json()['businesses']
    output = []
    for b in rest:
    	to_add = {}
    	to_add['name'] = b['name']
    	to_add['coordinate'] = b['location']['coordinate']
    	to_add['rating'] = b['rating']
    	output.append(to_add)
    return output

def get_search_parameters(lat,lon, rad):
    #See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat),str(lon))
    params["radius_filter"] = rad
    params["limit"] = "20"

    return params

def get_results(lat, lon, rad):
	params = get_search_parameters(lat, lon, rad)
	return get_results_from_params(params)