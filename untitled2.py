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
from plot import *


# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------

consumer_key = "KYg1pMmz4ID9vdMMxtdybUiad"
consumer_secret = "CkaBYGtYZghGfjADHx81rWWPMCQGnSvMQF4RHpX2yVeWe29Zgk"
access_key= "1596558961758859264-54eoTdv0bgOc3bvATLq7hgTYNWt0zg"
access_secret = "zfZM65WJkKpUwnliF6qF7NHexMKddg1d6PMql7H9ZIDsC"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
df=pd.DataFrame()
@app.route('/', methods=['GET', 'POST'])
def main():
    
    
    # If a form is submitted
    if request.method == "POST":
       
       search_query = request.form.get("search")
       tweets = tweepy.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              ).items(4)
       tweets_copy=clean(tweets)
       df= pola(tweets_copy)
       plot(df)
       #print(df[0][0])
      # li=list(df.itertuples(index=False))
       #print(df.to_string())
       return df.to_string()
      
       
       
    return render_template("index.html")
    
 #search query, whatever we want to search

# get tweets from the API

    
        
    

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