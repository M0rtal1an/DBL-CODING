import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect(r'C:\Users\20221859\Downloads\airlines.db')
cursor = connection.cursor()

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Retrieve the tweet data and direct replies using SQL queries
cursor.execute("SELECT id, user_verified FROM data_new WHERE in_reply_to_status_id IS NULL")
tweets = cursor.fetchall()

cursor.execute("SELECT id, sentiment_score, user_verified FROM data_new WHERE in_reply_to_status_id IS NOT NULL")
replies = cursor.fetchall()

# Store the verified and non-verified sentiment scores
verified_scores = []
non_verified_scores = []

# Perform sentiment analysis on the direct replies
for reply_id, reply_score, user_verified in replies:
    if reply_score is not None:
        if user_verified == 1:
            verified_scores.append(reply_score)
        else:
            non_verified_scores.append(reply_score)

# Calculate overall sentiment statistics
def calculate_sentiment_statistics(scores):
    if len(scores) > 0:
        average_score = sum(scores) / len(scores)
        min_score = min(scores)
        max_score = max(scores)
        return average_score, min_score, max_score
    else:
        return None, None, None

# Calculate sentiment statistics for verified and non-verified direct replies
verified_average, verified_min, verified_max = calculate_sentiment_statistics(verified_scores)
non_verified_average, non_verified_min, non_verified_max = calculate_sentiment_statistics(non_verified_scores)

# Print the sentiment analysis results
print("Verified User Impact:")
print(f"Average Sentiment: {verified_average}")
print(f"Minimum Sentiment: {verified_min}")
print(f"Maximum Sentiment: {verified_max}")
print()
print("Non-Verified User Impact:")
print(f"Average Sentiment: {non_verified_average}")
print(f"Minimum Sentiment: {non_verified_min}")
print(f"Maximum Sentiment: {non_verified_max}")

# Close the database connection
cursor.close()
connection.close()
