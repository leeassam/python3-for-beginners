#Dictionaries

movie = {
    "title" : "Inception",
    "rating" : "PG-13",
    "director" : "Christopher Nolan",
    "stars" : ["Leonardo DiCaprio", "Tom Hardy"]
}

#Extracting key values

print(movie["title"])
print(movie["stars"][1])

print (movie.get("title"))

#Change a value
movie["rating"] = "PG"

#Adding a value
movie["runtime"] = 200

print (movie)

#Loop through a dictionary

#print key names
for x in movie:
    print(x)

#print values
for x in movie:
    print(movie[x])

#Loop through keys and values
for x, y in movie.items():
    print(x,y)

#check if key exists
if "rating" in movie:
    print("The movie has a rating")

#Adding items
movie["year"] = 2010

print(movie)

#Removing items
movie.pop("year")

print(movie)

#Remove items with a specified keyword
del movie["rating"]

print(movie)

#Clear a dictionary

movie.clear()

print(movie)

#Delete the whole dictionary
del movie

#dict() Constructor
movie2 = dict (title="Matrix", rating = "PG-13", year=1999)

print(movie2)