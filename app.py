from flask import Flask, render_template, request, session, redirect, url_for, flash
import os, sqlite3, hashlib, json, requests, sys
import pymongo, json

app= Flask(__name__)
app.secret_key = os.urandom(64)

@app.route('/', methods=['POST', 'GET'])
def root():
    with open("movies.json", "r") as f:
        moviesList = json.load(f)
    connection = pymongo.MongoClient("homer.stuy.edu")
    connection.drop_database("leiGkalmakovaB")

    connection = pymongo.MongoClient("homer.stuy.edu")
    db = connection.leiGkalmakovaB
    collection = db.movies
    collection.insert_many(moviesList) 
    return render_template("form.html")
if __name__ == '__main__':
    app.debug = True
    app.run()

    ##collection = db.movies
    ##collection.insert_many(moviesList) 