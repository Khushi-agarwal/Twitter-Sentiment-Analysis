#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:29:20 2022

@author: khushiagarwal
"""


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


# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------

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
    
    
    # If a form is submitted
    """
    if request.method == "POST":
       
       search_query = request.form.get("search")
       tweets = tweepy.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              ).items(50)
       tweets_copy=clean(tweets)
       df= pola(tweets_copy)
       plot2(df)
       #print(df[0][0])
      # li=list(df.itertuples(index=False))
       #print(df.to_string())
       return df.to_string()
      """
       
       
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
    

    
    """
       # Unpickle classifier
        clf = joblib.load("classifier.pkl")
        
        # Get values through input bars
        hastag = request.form.get("search_query")
       
        # Put inputs to dataframe
        X = pd.DataFrame([[hastag]], columns = ["result"])
        
        # Get prediction
        prediction = "uygbuhbhub"
        
    else:
        prediction = "ihuibuin"
        """