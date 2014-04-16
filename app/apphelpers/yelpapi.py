#!/usr/bin/env python

"""
Module for interacting with yelp v2 api.
"""
import urllib2
import urllib
import os
import re
import json
import oauth2

CONSUMER_KEY = 'AAw9DLCB_H2ALIyzdtu4MQ'
CONSUMER_SECRET = 'CkQR6RoZBGbr0r2L7dIGP0rIFJs'
TOKEN = 'CsCyhsvVqiLb9K7S4QEhl5BpdxpEKw1G'
TOKEN_SECRET = 'VCjgwlibBHVmY4rIzqoKsUW2ZmE'
API_URL = "api.yelp.com"

def _yelp_api_request(host, path, url_params, consumer_key,
                      consumer_secret, token, token_secret):
    """Returns response for API request."""
    # Unsigned URL
    encoded_params = ''
    if url_params:
        encoded_params = urllib.urlencode(url_params)
    url = 'http://%s%s?%s' % (host, path, encoded_params)
    print 'URL: %s' % (url,)

    # Sign the URL
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': token,
                          'oauth_consumer_key': consumer_key})

    token = oauth2.Token(token, token_secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(),
                               consumer, token)
    signed_url = oauth_request.to_url()
    print 'URL: %s' % (signed_url,)
    # Connect
    try:
        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()
    except urllib2.HTTPError, error:
        response = json.loads(error.read())

    return response

def find_business_by_id(businessid):
    """
    Get business information by id.

    Parameters
    ----------
    businessid: a unique business id.

    Returns
    -------
    A JSON object including all information about this business.
    """
    response = _yelp_api_request(API_URL,
                                 '/v2/business/%s' % businessid,
                                 {},
                                 CONSUMER_KEY,
                                 CONSUMER_SECRET,
                                 TOKEN,
                                 TOKEN_SECRET)
    return response

