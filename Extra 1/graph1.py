import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
connection = sqlite3.connect(r'C:\Users\20221859\Downloads\airlines (1).db')
cursor = connection.cursor()

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Retrieve the tweet data and direct replies using SQL queries
cursor.execute("SELECT t.sentiment_score, r.sentiment_score "
               "FROM data_new AS t "
               "LEFT JOIN data_new AS r ON t.id = r.in_reply_to_status_id "
               "WHERE t.in_reply_to_status_id IS NULL AND r.user_verified = 1 "
               "AND t.user_name NOT IN ('British Airways', 'American Airlines', 'Virgin Atlantic', "
               "'Lufthansa', 'easyJet', 'Ryanair', 'Royal Dutch Airlines', 'Air France')")
data = cursor.fetchall()

# Close the database connection
cursor.close()
connection.close()

# Store the sentiment scores for tweets and replies
verified_sentiments = []
change_sentiments = []

# Perform sentiment analysis on the data and calculate the change in sentiment
for row in data:
    if len(row) >= 2:
        tweet_score = row[0]
        reply_score = row[1]
        if tweet_score is not None and reply_score is not None:
            verified_sentiments.append(tweet_score)
            change_sentiments.append(tweet_score - reply_score)

# Plot the scatter plot
plt.scatter(verified_sentiments, change_sentiments, alpha=0.5)
plt.xlabel('Sentiment of Verified Tweet')
plt.ylabel('Change in Conversation Sentiment')
plt.title('Change in Sentiment due to Verified User Interaction')
plt.show()
