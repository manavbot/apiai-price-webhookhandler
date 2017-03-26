#!/usr/bin/env python

import json
import os

from flask import Flask
from flask import request

from gmaps import GoogleMaps
from uber import Uber
from lyft import Lyft

# Flask app should start in global layout
app = Flask(__name__)

# @app.route('/')
# def home():
#     return 0

@app.route('/webhook', methods=['GET'])
def webhook():
    # data = str(request.form['data'])
    # print(data + "data")
    # google_maps_results = GoogleMaps("2184 Pettigrew Dr", "4269 Littleworth Way")
    uber_results = Uber(12)
    lyft_results = Lyft(12)
    res = makeWebhookResult(uber_results, lyft_results)
    return json.dumps(res)


def makeWebhookResult(uber_results, lyft_results):
    speech = "The cost is " + str(uber_results) + " for uber and " + str(lyft_results) + " for lyft."
    
    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-price-webhookhandler"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
