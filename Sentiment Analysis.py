import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect(r'C:\Users\20221859\Downloads\airlines.db')

# Retrieve the tweet data using a SQL query
query = "SELECT id, text FROM data_new"
alter_query = "ALTER TABLE data_new ADD COLUMN sentiment_score FLOAT"  # Add a new column for sentiment score
alter_query2 = "ALTER TABLE data_new ADD COLUMN sentiment_label TEXT"  # Add a new column for sentiment label
cursor = connection.cursor()
cursor.execute("PRAGMA table_info(data_new)")
columns = cursor.fetchall()
column_names = [column[1] for column in columns]
if 'sentiment_score' not in column_names:
    cursor.execute(alter_query)
if 'sentiment_label' not in column_names:
    cursor.execute(alter_query2)
cursor.execute(query)
tweets = cursor.fetchall()

# Initialize the VADER sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

tweet_count = 0

# Iterate over the retrieved tweets
for tweet in tweets:
    tweet_count += 1
    tweet_id = tweet[0]
    tweet_text = tweet[1]

    # Perform sentiment analysis on the tweet
    sentiment_scores = sia.polarity_scores(tweet_text)
    compound_score = sentiment_scores['compound']

    # Assign a sentiment label based on the compound score
    if compound_score >= 0.05:
        sentiment_label = 'Positive'
    elif compound_score <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Update the database with the sentiment score
    update_query = f"UPDATE data_new SET sentiment_score = {compound_score} WHERE id = {tweet_id}"
    cursor.execute(update_query)
    connection.commit()

    # Progress
    print(f"Processed tweet {tweet_count}/{len(tweets)}")

# Close the database connection
cursor.close()
connection.close()
