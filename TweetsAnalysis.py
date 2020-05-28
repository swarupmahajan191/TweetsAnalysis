from typing import re
import re 
import tweepy
import csv
from textblob import TextBlob
import pandas as pd
import nltk

##input your credentials here
consumer_key = 'RHoQHLuzrlTWmcFnWbyQakDIO'
consumer_secret = 'NnjyTaDgxSJMGnTFoX7XJoL3x75hQN5tW4E88W1NjN12REidFF'
access_token = '925727750198931461-K36R4AvbezaElKIOBuHvTiMfKptbcFY'
access_token_secret = "frALDWd7cPyz9fLn6thgnRyqnagTzQ9icjXaoLdM7jqdi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []

# append all tweet data to list
for tweet in tweepy.Cursor(api.search,q="#atmnirbhar",count=100).items():
    tweets.append(tweet)

# convert 'tweets' list to pandas.DataFrame
tweets_df = pd.DataFrame((vars(tweets[i]) for i in range(len(tweets))),columns=['text'])

# define file path (string) to save csv file to
FILE_PATH = "C:/Users/HMS_Android/Desktop/Swarup/TweetsAnalysis/TweetsAnalysisFile.csv"

# use pandas to save dataframe to csv
tweets_df.to_csv(FILE_PATH)
df_survey_data = pd.read_csv("TweetsAnalysisFile.csv")
COLS = ['text', 'sentiment','subjectivity','polarity']
df = pd.DataFrame(columns=COLS)

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

for index, row in nltk.islice(df_survey_data.iterrows(), 0, None):
    new_entry1 = []
    new_entry = []

    text_lower =((row['text']))
    blob = TextBlob(clean_tweet(text_lower))
    sentiment = blob.sentiment

    csvFile = open('TweetsAnalysis-Positive.csv', 'a')
    csvWriter = csv.writer(csvFile)

    csvFile2 = open('TweetsAnalysis-Negative.csv', 'a')
    csvWriter2 = csv.writer(csvFile2)
    if sentiment[0] > 0:
        csvWriter.writerow([text_lower.encode('utf-8')])
        print('Positive')
    else:
        csvWriter2.writerow([text_lower.encode('utf-8')])
     
        print('Negative')
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    new_entry += [text_lower, sentiment, subjectivity, polarity]



