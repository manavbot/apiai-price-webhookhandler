import urllib2
import json
from uber_rides.session import Session


def Uber(data):
	request_headers = {
		"Authorization": "Token VG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS" 
	}

	session = Session(server_token = "sVG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS")

	request = urllib2.Request("https://api.uber.com/v1.2/estimates/price?start_latitude=37.7752315&start_longitude=-122.418075&end_latitude=37.7752415&end_longitude=-122.518075", headers = request_headers)
	content = urllib2.urlopen(request).read()	
	jsoncontent = json.loads(content)
	print(jsoncontent)

	prices = jsoncontent['prices']
	if prices is None:
		return {}

	estimate = prices[1]['estimate']
	if estimate is None:
		return {}

	print("Estimate", estimate)
	return estimate
