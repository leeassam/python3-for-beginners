#HTTP requests
import requests
import json
from requests.exceptions import HTTPError

#Making a GET request
#r = requests.get('https://www.google.com')

'''
r.status_code - HTTP status code
r.headers - HTTP headers
r.text - Response text
'''
'''
print(r.status_code)
print(r.headers)

print("\n")
print(r.text)

#Downloading and saving an image
#Python logo

imageData = requests.get("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png")
with open('logo.png', 'wb') as i:
    i.write(imageData.content)
'''
#passing in arguments (query string parameters) in our get request
'''
#Search GitHub's repositories using a GET Request
response = requests.get (
    'https://api.github.com/search/repositories',
    params={'q' : 'requests+language:python'}
)

#Inspect some attributes of the requests repository
json_response = response.json()
print("Result")
repository = json_response['items'][0]
print(f'Repository Name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')
'''

#Making an Http request to openweathermap
parameters = {"q" : "Atlanta", "units" : "imperial", "appid" : "05ac287f378f9a869f11e94ddc52701f"}
r = requests.get("https://api.openweathermap.org/data/2.5/weather" , params=parameters)

print(r.text)

#load result in a json object
weather = json.loads(r.text)
print(f"The temperature in {weather['name']} is: {weather['main']['temp']} F")

#Determining if an error occurred
parameters = {"q" : "New York", "units" : "imperial", "appid" : "05ac287f378f9a869f11e94ddc52701f"}

try :
    r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
    #if r.status_code != 200:
    if r.status_code != requests.codes.ok :
        r.raise_for_status()
    print(r.text)
except HTTPError as error:
    print ("An exception occurred: " + str(error))
except Exception as e:
    print (f'Other exception occurred {e}')


#POST requests
payload = { "data": "Post data to send"}
resp = requests.post("https://postman-echo.com/post", data=payload)

print(resp.status_code)

obj = resp.json()
#obj = json.loads(resp.text)

print(obj)