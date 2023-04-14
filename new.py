#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:03:24 2023

@author: khushiagarwal
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:54:37 2022

@author: khushiagarwal
"""
"""
access token=1596558961758859264-54eoTdv0bgOc3bvATLq7hgTYNWt0zg
access token secret=zfZM65WJkKpUwnliF6qF7NHexMKddg1d6PMql7H9ZIDsC
api key="KYg1pMmz4ID9vdMMxtdybUiad"
api key secret="CkaBYGtYZghGfjADHx81rWWPMCQGnSvMQF4RHpX2yVeWe29Zgk"
bearer token=AAAAAAAAAAAAAAAAAAAAAOwPjwEAAAAAPoyWjAxQ3lRPWuT9qxyPs65wKDg%3D6kYl5ZAOrJpA4PkjtyjEdlSDqzoXT0ewfegGUXsXsfr89mJp5u
"""

 
import pandas as pd
import csv

import string
import preprocessor as p
from textblob import TextBlob
from matplotlib import pyplot as plt
import tweepy  
import re 

def analysis(score):
    if(score<0):
        return 'Negative'
    elif(score==0):
        return 'Neutral'
    else:
       return 'Positive'
def clean(tweets):
    
    copy=[]
    for tweet in tweets:
   
        """
        text=tweet.text
        text=re.sub(r'@[A-Za-z0-9]+','',text) #Removed @mentions
        text=re.sub(r'#','',text) #Removing the # symbol
        text=re.sub(r'RT[\s]+','',text) #removing rt
        text=re.sub(r'https?:\/\/\S+','',text) #removing the hyperlink
        """
       # print(tweet.text,'\n')
       # text = re.sub(r'https?://[^ ]+', '', text)
        
        transf = re.sub(r'https?://[^ ]+', '', tweet.text) # tweet.text is used to convert status object to string and link is being removed
        transf=re.sub(r'@[A-Za-z0-9]+','',transf) 
       # transf = re.sub(r' 0 ', 'zero', transf) #Punctuations and numbers
        transf = re.sub(r'[^A-Za-z ]', '', transf)#puctuations and numbers
        transf =re.sub(r'RT[\s]+','',transf)
       # transf=transf.lower()# converting all in lower
      #  print(transf,'\n'," ")   
        #print(text,1,"\n"
        copy.append(transf)
    return copy

"""
consumer_key = "KYg1pMmz4ID9vdMMxtdybUiad"
consumer_secret = "CkaBYGtYZghGfjADHx81rWWPMCQGnSvMQF4RHpX2yVeWe29Zgk"
access_key= "1596558961758859264-54eoTdv0bgOc3bvATLq7hgTYNWt0zg"
access_secret = "zfZM65WJkKpUwnliF6qF7NHexMKddg1d6PMql7H9ZIDsC"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

 
api = tweepy.API(auth)

search_query="#"   #search query, whatever we want to search

# get tweets from the API
tweets = tweepy.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              ).items(150)  # number of tweets to be extracted

# store the API responses in a list
tweets_copy = []
tweets_copy=clean(tweets)
"""


  
#print(tweets_copy)

   # transf = re.sub(r'https?://[^ ]+', '', tweet.text) # tweet.text is used to convert status object to string and link is being removed
   
    #transf = re.sub(r' 0 ', 'zero', transf) #Punctuations and numbers
    #transf = re.sub(r'[^A-Za-z ]', '', transf)#puctuations and numbers
   # transf=transf.lower()# converting all in lower
   # print(transf,'\n'," ")   
def pola(tweets_copy):
    df=pd.DataFrame()
    pol=[]
    subject=[]    
    for t in tweets_copy:
        print(t,'\n')
    
    df['Tweets']=tweets_copy

    for t in tweets_copy:
        subject.append(TextBlob(t).sentiment.subjectivity)
        pol.append(TextBlob(t).sentiment.polarity)

    df['Subjectivity']=subject
    df['Polarity']=pol
    df['Analysis']=df['Polarity'].apply(analysis)
    print(df)
    return df

def plot2(df):
    print(df)
   
    plt.figure(figsize=(8,6))
    for i in range(0,df.shape[0]):
       
        plt.scatter(df['Polarity'][i],df['Subjectivity'][i],color="Red")

    plt.title('Sentiment')
    plt.xlabel('Polarity')
    plt.ylabel('Subjectivity')
    plt.show()
    print("I am plot")
    positive=df[df.Analysis=='Positive']
    positive=positive['Tweets']
    df['Analysis'].value_counts()
    plt.title('Review')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    df['Analysis'].value_counts().plot(kind='pie')
    plt.show()
    x=[1,2,3]
    y=[3,4,5]
    plt.plot(x,y)
    plt.show()

    
    #print("Total Tweets fetched:", len(tweets_copy))

#print(round((positive.shape[0]/df.shape[0])*100,1))

#print(subject)
#print(pol)

    

   


    
 
"""
username_tweets = tweepy.Cursor(api.search_tweets, q="@elonmusk", tweet_mode='extended').items(5)
for tweet in username_tweets:
    text = tweet._json["full_text"]
    print(text)
    
csvWriter = csv.writer(csvFile)
 
search_words = "kohli"      # enter your words
new_search = search_words + " -filter:retweets"
 
for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
"""