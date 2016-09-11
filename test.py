import request
import estimates

def get_ride_details():

	lat1 = 39.952
	lng1 = -75.165

	origin = estimates.get_location()

	lat2 = origin['lat']
	lng2 = origin['lng']
	friends = 1

	print("READY TO REQUEST RIDE")

	response = request.request_ride(lat2, lng2, lat1, lng1, friends)

	print("RESPONSE HAS BEEN RECEIVED")

	return response

