import googlemaps
from datetime import datetime

def GoogleMaps(starting_location, ending_location):
	maps = googlemaps.Client(key='AIzaSyCBW43NX5azxoLmUKD1vZiZxbqGaG9NUGo')

	# Geocoding an address
	geocode_starting_location = maps.geocode(starting_location)
	geocode_ending_location = maps.geocode(ending_location)
	print("Start: ", geocode_starting_location)
	print("End: ", geocode_ending_location)
	return [geocode_starting_location, geocode_ending_location]
