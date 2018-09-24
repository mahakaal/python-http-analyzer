#!/usr/bin/env python3

import requests
import sys
import pprint

__author__ = "Sukhdev Mohan"
__version__ = "1.0.0"
__licence__ = "GPL"
__email__ = "sukhdev.mohan@gmail.com"

"""
This is a simple utility script, to analyze HTTP requests and responses.
"""

print("Python HTTP request/Response Analyzer.\nThis utility script takes in input an URL and prints:\n1. The URL\n2. HTTP request status\n3. Server response header\n4. Server Response header\n5. Content in JSON format\n6. Content in TEXT format")
print("The utility is provided by Sukhdev Mohan <sukhdev.mohan@gmail.com> under GPL licence.")

url = input("Enter an URL (please insert also the protocol): ")
print('---------------------------------\nRequesting URL: ' + url)

httpObject = requests.get(url)

print("---------------------------------\nRequest Status Code: " + str(httpObject.status_code))

pp = pprint.PrettyPrinter(indent=4)
print("---------------------------------\nRequest from User to Server:")
pp.pprint(httpObject.request.headers)

print("---------------------------------\nResponse from Server to User:")
pp.pprint(httpObject.headers)

print("---------------------------------\nJSON:")
pp.pprint(httpObject.json())

print("---------------------------------\nTEXT:")
pp.pprint(httpObject.text)
