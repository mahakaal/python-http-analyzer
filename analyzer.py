#!/usr/bin/env python3

import requests
import sys
import pprint
import datetime
__author__ = "Sukhdev Mohan"
__version__ = "1.0.0"
__licence__ = "GPL"
__email__ = "sukhdev.mohan@gmail.com"

"""
This is a simple utility script, to analyze HTTP requests and responses.
"""

print("Python HTTP request/Response Analyzer.\nThis utility script takes in input an URL and prints:\n1. The URL\n2. HTTP request status\n3. Server response header\n4. Server Response header\n5. Content in JSON format\n6. Content in TEXT format")
print("The utility is provided by Sukhdev Mohan <sukhdev.mohan@gmail.com> under GPL licence. The utility will automativally generate a report file, in addition to the terminal printout.")

url = input("Enter an URL (please insert also the protocol): ")

report = open('pha-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt', 'w+')

print('---------------------------------\nRequesting URL: ' + url)
report.write('\n---------------------------------\nRequesting URL: ' + url)

httpObject = requests.get(url)

print("---------------------------------\nRequest Status Code: " + str(httpObject.status_code))
report.write("\n---------------------------------\nRequest Status Code: " + str(httpObject.status_code))

pp = pprint.PrettyPrinter(indent=4)
ppf = pprint.PrettyPrinter(indent=4, stream=report)
print("---------------------------------\nRequest from User to Server:")
report.write("\n---------------------------------\nRequest from User to Server:")
pp.pprint(httpObject.request.headers)
ppf.pprint(httpObject.request.headers)

print("---------------------------------\nResponse from Server to User:")
report.write("\n---------------------------------\nResponse from Server to User:")
pp.pprint(httpObject.headers)
ppf.pprint(httpObject.headers)

print("---------------------------------\nJSON:")
report.write("\n---------------------------------\nJSON:")
pp.pprint(httpObject.json())
ppf.pprint(httpObject.json())

print("---------------------------------\nTEXT:")
report.write("\n---------------------------------\nTEXT:")
pp.pprint(httpObject.text)
ppf.pprint(httpObject.text)
