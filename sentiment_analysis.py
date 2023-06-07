import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('C:/GIT DBL1/airlines.db')

# Retrieve the tweet data using a SQL query
query = """SELECT id, text, user_id FROM data_new WHERE user_id NOT IN (18332190, 22536055, 124476322, 20626359,
        106062176, 1542862735, 38676903, 253340062, 56377143) and sentiment_score IS NULL"""
alter_query = "ALTER TABLE data_new ADD sentiment_score FLOAT"
cursor = connection.cursor()
cursor.execute("PRAGMA table_info(data_new)")
columns = cursor.fetchall()
column_names = [column[1] for column in columns]
if 'sentiment_score' not in column_names:
    cursor.execute(alter_query)
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

    # Update the database with the sentiment score
    update_query = f"UPDATE data_new SET sentiment_score = {compound_score} WHERE id = {tweet_id}"
    cursor.execute(update_query)
    connection.commit()

    print(f"Processed tweet {tweet_count}/{len(tweets)}")

# Close the database connection
cursor.close()
connection.close()