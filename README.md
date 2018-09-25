# Python HTTP request/Response Analyzer.
This utility script takes in input an URL and prints:
1. The URL
2. HTTP request status
3. Server response header
4. Server Response header
5. Content in JSON format
6. Content in TEXT format

The utility is provided by Sukhdev Mohan <sukhdev.mohan@gmail.com> under GPL licence.

The script automatically dump a report with today's datetime.
# Usage
```
python3 analyzer.py
```
and follow the instructions

## Example

Lets say you want to test you API which sends you a JSON response. I've chosen a random JSON generator and mockup site from google:
```
 https://jsonplaceholder.typicode.com/todos/1
```
Launch the script with command above

```
python3 analyzer.py
```

then insert the API's URL ( https://jsonplaceholder.typicode.com/todos/1 ) and you should see a response like this:
```
Python HTTP request/Response Analyzer.
This utility script takes in input an URL and prints:
1. The URL
2. HTTP request status
3. Server response header
4. Server Response header
5. Content in JSON format
6. Content in TEXT format
The utility is provided by Sukhdev Mohan <sukhdev.mohan@gmail.com> under GPL licence. The utility will automativally generate a report file, in addition to the terminal printout.
Enter an URL (please insert also the protocol):  https://jsonplaceholder.typicode.com/todos/1
---------------------------------
Requesting URL:  https://jsonplaceholder.typicode.com/todos/1
---------------------------------
Request Status Code: 200
---------------------------------
Request from User to Server:
{'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
---------------------------------
Response from Server to User:
{'Date': 'Tue, 25 Sep 2018 14:03:25 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d95072b708862df59904d07762bcaef2c1537884205; expires=Wed, 25-Sep-19 14:03:25 GMT; path=/; domain=.typicode.com; HttpOnly', 'X-Powered-By': 'Express', 'Vary': 'Origin, Accept-Encoding', 'Access-Control-Allow-Credentials': 'true', 'Cache-Control': 'public, max-age=14400', 'Pragma': 'no-cache', 'Expires': 'Tue, 25 Sep 2018 18:03:25 GMT', 'X-Content-Type-Options': 'nosniff', 'Etag': 'W/"53-hfEnumeNh6YirfjyjaujcOPPT+s"', 'Via': '1.1 vegur', 'CF-Cache-Status': 'HIT', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Server': 'cloudflare', 'CF-RAY': '45fe08be4f3d72a1-AMS', 'Content-Encoding': 'gzip'}
---------------------------------
JSON:
{'completed': False, 'id': 1, 'title': 'delectus aut autem', 'userId': 1}
---------------------------------
TEXT:
('{\n'
 '  "userId": 1,\n'
 '  "id": 1,\n'
 '  "title": "delectus aut autem",\n'
 '  "completed": false\n'
 '}')
```
