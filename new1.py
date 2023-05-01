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
from new import clean
from new import pola
from new import plot2



consumer_key = "FoxhZf5AFjWHhDBggBkHgpbrx"
consumer_secret = "kLnB5EjssvyMYYbbH1C13YJScOmy310OUDCuDANKiqYq9dHtqM"
access_key= "1596558961758859264-jFbu3uG6pN8JeAL4NAkVlQqXfLGMJt"
access_secret = "GCf3z6pQw6bLO74bd0meuvYlBOG9z3dH1FkMXxp4YJ7zg"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
df=pd.DataFrame()

def result():
    
    
    # If a form is submitted
   
       
       search_query = 'msd'
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
       #return df.to_string()
      


    
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