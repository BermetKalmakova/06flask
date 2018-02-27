from flask import Flask, render_template, request, session, redirect, url_for, flash
import os, sqlite3, hashlib, json, requests, sys
import pymongo, json
from movies import queryTitle, queryDirector, queryGenre, queryYear

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
    ## I dont know why request.form['title'] etc. is giving me a bad request so I used request.form.get('title') etc. instead
    boolean = request.form.get('title') != "" or request.form.get('genre') != "" or request.form.get('year') != "" or request.form.get('director') != ""

    ## I dont know why request.form['title'] etc. is giving me a bad request so I used request.form.get('title') etc. instead
    if ((request.method == 'POST' or  request.method == 'GET') and boolean):
        if (request.form.get('title') != ""):
            querySearch = request.form.get('title')
            return render_template('form.html', info = queryTitle(querySearch))
        if (request.form.get('genre') != ""):
            querySearch = request.form.get('genre')
            return render_template('form.html', info = queryGenre(querySearch))
        if (request.form.get('year') != ""):
            querySearch = request.form.get('year')
            return render_template('form.html', info = queryYear(querySearch))
        if (request.form.get('director') != ""):
            querySearch = request.form.get('director')
            return render_template('form.html', info = queryDirector(querySearch))
    else:
        return render_template('form.html')
    ## return render_template("form.html")

if __name__ == '__main__':
    app.debug = True
    app.run()

    ##collection = db.movies
    ##collection.insert_many(moviesList) 