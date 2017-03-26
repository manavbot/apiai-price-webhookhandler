import googlemaps

def GoogleMaps(starting_location, ending_location):
	gmaps = googlemaps.Client(key='AIzaSyCOlweck6eXODDMta-HgidoYqhM3GQ9XOE')
	geocode_starting_location = maps.geocode(starting_location)
	geocode_ending_location = maps.geocode(ending_location)
	print("Start: ", geocode_starting_location)
	print("End: ", geocode_ending_location)
	return [geocode_starting_location, geocode_ending_location]
