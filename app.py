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
    #data = priceEstimate()
    data = 5
    print (data)
    res = makeWebhookResult(data)
    print (res)
    
    
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    print (r)
    return r



def makeWebhookResult(data):
    estimate = data
    speech = "The cost is " + estimate 
    
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

    app.run(debug=False, port=port, host='0.0.0.0')
