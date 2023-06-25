import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Connect to the SQLite database
connection = sqlite3.connect(r'C:\Users\20221859\Downloads\airlines (1).db')
cursor = connection.cursor()

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Retrieve the tweet data and direct replies from verified users (excluding airlines) using SQL queries
cursor.execute("SELECT t.id, t.sentiment_score, t.user_verified, r.sentiment_score "
               "FROM data_new AS t "
               "LEFT JOIN data_new AS r ON t.id = r.in_reply_to_status_id "
               "WHERE t.in_reply_to_status_id IS NULL "
               "AND r.user_verified = 1 "
               "AND t.user_name NOT IN ('British Airways', 'American Airlines', 'Virgin Atlantic', "
               "'Lufthansa', 'easyJet', 'Ryanair', 'Royal Dutch Airlines', 'Air France')")
data = cursor.fetchall()


# Store the sentiment scores for tweets and replies
tweet_sentiments = []
reply_sentiments = []

# Perform sentiment analysis on the data
for tweet_id, tweet_score, user_verified, reply_score in data:
    if tweet_score is not None and reply_score is not None:
        tweet_sentiments.append(tweet_score)
        reply_sentiments.append(reply_score)

# Close the database connection
cursor.close()
connection.close()


# Plot the scatter plot
plt.scatter(tweet_sentiments, reply_sentiments, alpha=0.5)
plt.xlabel('Sentiment before Verified User Reply')
plt.ylabel('Sentiment after Verified User Reply')
plt.title('Sentiment Before and After Verified User Reply')
plt.show()



