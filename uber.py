import urllib2
from uber_rides.session import Session

def Uber(data):
	request_headers = {
		"Authorization": "Token VG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS" 
	}

	session = Session(server_token = "sVG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS")

	request = urllib2.Request("https://api.uber.com/v1.2/estimates/price?start_latitude=37.7752315&start_longitude=-122.418075&end_latitude=37.7752415&end_longitude=-122.518075", headers = request_headers)
	content = urllib2.urlopen(request).read()

	prices = content.get('prices')
    if prices is None:
        return {}

    localized_display_name = prices[1].get('localized_display_name')
    if localized_display_name is None:
        return {}

    estimate = localized_display_name.get('estimate')
    if estimate is None:
        return {}

	print(estimate)
	return estimate	
