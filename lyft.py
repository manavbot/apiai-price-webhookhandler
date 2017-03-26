import urllib2
import json
from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session
  
def Lyft(data):
	auth_flow = ClientCredentialGrant(
    	"Fgmhjllzla10",
    	"IJYdH-tIxextpZxjSdxe0uBFaWwt-u9_",
    	"public",
    )

	headers = {
		'Content-Type': 'application/json'
	}

	data = '{"grant type": "client_credentials", "scope":"public"}'
	users = '{"Fgmhjllzla10": "IJYdH-tIxextpZxjSdxe0uBFaWwt-u9_"}'

	authreq = urllib2.Request("https://api.lyft.com/oauth/token", headers=headers, data=data)
	accesstoken = urllib2.urlopen(authreq).read()

	# print "Access token:" + accesstoken

	# session = auth_flow.get_session()
	# request_headers = {
	# 	"Authorization": "Bearer " + accesstoken 
	# }

	# session = Session(server_token = "sVG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS")

	# request = urllib2.Request("https://api.uber.com/v1.2/estimates/price?start_latitude=37.7752315&start_longitude=-122.418075&end_latitude=37.7752415&end_longitude=-122.518075", headers = request_headers)
	# content = urllib2.urlopen(request).read()	
	# jsoncontent = json.loads(content)
	# print(jsoncontent)

	# prices = jsoncontent['prices']
	# if prices is None:
	# 	return {}

	# estimate = prices[1]['estimate']
	# if estimate is None:
	# 	return {}

	# print("Estimate", estimate)
	# return estimate
