#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "PrintUberData":
        return {}
    baseurl = "https://api.uber.com/v1.2/estimates/time?start_latitude=37.7752315&start_longitude=-122.418075"
    yql_query = None
    if yql_query is None:
        return {}
    yql_url = baseurl + "&format=json"
    result = urlopen(yql_url).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res



def makeWebhookResult(data):
    times = data.get('times')
    if times is None:
        return {}

    localized_display_name = times[2].get('localized_display_name')
    if localized_display_name is None:
        return {}
    

    estimate = localized_display_name.get('estimate')
    if estimate is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech = "The estimated arrival time for uber is " + estimate + " seconds." 
    
    #speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
     #        ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-uber-webhook"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
