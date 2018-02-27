
## download link: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
##  American Movies Scrapped from America 

## JSON contains: title, year, director,cast, genre, and notes

##
## We imported by importing the json module
##  Then we open the json and used a variable to hold the json contents (this variable is a list)
##  Using insert_many we inserted everything in the list into the database. 
##
##

import pymongo, json
with open("movies.json", "r") as f:
    moviesList = json.load(f)

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.leiGkalmakovaB 
collection = db.movies
collection.insert_many(moviesList) 


def queryTitle(title):
    queryList = collection.find({"title": title})
    return queryList

def queryYear(year):
    queryList = collection.find({"year": year})
    s = ""
    for each in queryList:
        s = s + each["title"] + ", " + str(each["year"]) + "; "
    return s

def queryDirector(director):
    queryList = collection.find({"director": director})
    return queryList

def queryGenre(genre):
    queryList = collection.find({"genre": genre})
    return queryList

##def queryInclusiveBetweenYears(y1,y2):
##    queryList = []
##    for each in collection.find({"$and": [{"year":{"$lte": y2}}, {"year":{"$gte": y1}}]}):
##        #print each
##        queryList.extend(each)
##    return queryList

##queryTitle("After Dark in Central")
##queryYear(1900)
##queryDirector("James H. White")
##queryGenre("Short")
##queryInclusiveBetweenYears(1900,1902)
