#Deserialization - Taking JSON and turning JSON encoded data into Python Objects
import json

with open ("movies.json") as movies_file:
    data = json.load(movies_file)

print(data)
print(data[1]["title"])
print(data[1]["actors"])

print("\n")

for obj in data:
    for x,y in obj.items():
        print(x,y)
    print("\n")

#to load from a string, use loads()

#Serialization - Taking a Python Object and converting it to a
# string or writing to a file

country_data = {
    "countries" : [
        {
            "country-code" : "TT",
            "name" : "Trinidad and Tobago",
            "population" : 1400000,
            "language" : "English",
            "capital" : "Port of Spain",
            "flag-colors" : ["red", "white", "black"]

        },
        {
            "country-code" : "US",
            "name": "United States of America",
            "population": 329000000,
            "language": "English",
            "capital" : "Washington, D.C.",
            "flag-colors": ["red", "white", "blue"]

        },
        {
            "country-code" : "MX",
            "name": "Mexico",
            "population": 127000000,
            "language": "Spanish",
            "capital" : "Mexico City",
            "flag-colors": ["red", "white", "green"]

        }
    ]
}

#writing to a file
with open ("countries.json", "w") as write_file:
    json.dump(country_data, write_file)

#writing to a string
json_string = json.dumps(country_data, indent=2)

print(json_string)