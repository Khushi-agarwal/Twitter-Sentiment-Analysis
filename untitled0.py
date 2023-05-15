#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:51:10 2023

@author: khushiagarwal
"""


from flask import Flask, render_template, request, redirect

import sqlite3

import threading
import sqlite3

from flask import Flask, request, render_template
import pandas as pd
import joblib
import tweepy
from new import *
#from new import pola
#from new import plot2
import os
import base64
from io import BytesIO
from matplotlib import pyplot as plt
from PIL import Image

# Create a thread-local storage object for the database connection and cursor
local = threading.local()

def get_conn():
    """
    Create a new database connection for the current thread, or return an existing one.
    """
    if not hasattr(local, 'conn'):
        local.conn = sqlite3.connect('/Users/khushiagarwal/Desktop/users.db')
    return local.conn

def get_cursor():
    """
    Create a new database cursor for the current thread, or return an existing one.
    """
    if not hasattr(local, 'cursor'):
        local.cursor = get_conn().cursor()
    return local.cursor






app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    # Insert the new user data into the database
    c = get_cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    # Commit the changes to the database
    user=c.fetchone()
    password=c.fetchone()
    get_conn().commit()
    if(user and password):
        return render_template('index.html', msg="Successfully signed in,now you can login!!")
    else:
        return render_template('index.html', msg="Try again!")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Query the database for the user with the given username and password
    c = get_cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    password=c.fetchone()
    error="Incorrect username or password"
    if user is None:
        return render_template('index.html', error=error)
    else:
        return main()
consumer_key = "FoxhZf5AFjWHhDBggBkHgpbrx"
consumer_secret = "kLnB5EjssvyMYYbbH1C13YJScOmy310OUDCuDANKiqYq9dHtqM"
access_key= "1596558961758859264-jFbu3uG6pN8JeAL4NAkVlQqXfLGMJt"
access_secret = "GCf3z6pQw6bLO74bd0meuvYlBOG9z3dH1FkMXxp4YJ7zg"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
df=pd.DataFrame()
@app.route('/', methods=['GET', 'POST'])
def main():
    
    
  
       
       
    return render_template("newindex.html")
    
 #search query, whatever we want to search

# get tweets from the API

@app.route('/results', methods=['GET', 'POST'])
def result():
    
    
    # If a form is submitted
    #if request.method == "POST":
    search_query = request.form.get("search")
    count=int(request.form.get("count"))
    tweets = tweepy.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              ).items(count)
   # print(tweets)
    tweets_copy=clean1(tweets)
    df= pola(tweets_copy)
    encoded_img_bar=bar(df)
    encoded_img_data=plot2(df)
    encoded_img_subpo=subpo(df)
    num_rows,num_cols=df.shape
   
       #plot_url = base64.b64encode(img.getvalue()).decode('utf8')
     
    return render_template('results.html',img_bar=encoded_img_bar.decode('utf-8'),img_data=encoded_img_data.decode('utf-8'),img_subpo=encoded_img_subpo.decode('utf-8'),count=num_rows,df=df)
"""
@app.after_request
def delete(response):
    os.remove('static/images/analysis.png')
    return response

"""        
    

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
    

if __name__ == '__main__':
    app.run(debug=True)
