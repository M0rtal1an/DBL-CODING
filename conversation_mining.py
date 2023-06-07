import numpy as np
import pandas as pd
import sqlite3
import json
import os


def get_tweet_sequences(database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Create a dictionary to store the sequences
    tweet_conversations = {}

    # Execute a SELECT query to fetch all tweets
    cursor.execute("SELECT id, CAST(in_reply_to_status_id AS INTEGER) AS in_reply_to_status_id, in_reply_to_user_id, user_id FROM data_new")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Traverse the rows
    for row in rows:
        tweet_id = row[0]
        reply_to_id = row[1]
        reply_to_user = row[2]
        user_id = row[3]

        # Check if the tweet is a reply
        if reply_to_id == 0:
            # If the tweet is not a reply, create a new sequence with only the current tweet
            tweet_conversations[tweet_id] = [tweet_id]
        else:

            # Check if the reply is already part of a sequence
            if reply_to_id in tweet_conversations:
                # Append the current tweet to the existing sequence
                sequence = tweet_conversations[reply_to_id]
                sequence.append(tweet_id)
            else:
                # Create a new sequence with the reply and the current tweet
                sequence = [reply_to_id, tweet_id]
                tweet_conversations[reply_to_id] = sequence
    # Close the database connection
    cursor.close()
    conn.close()

    # Return the tweet sequences
    return tweet_conversations

# Example usage:
database_path = 'C:/GIT DBL1/airlines.db'
conversations = get_tweet_sequences(database_path)

for sequence_id, conversation in conversations.items():
    if len(conversation) > 3:
        print(f"Conversation {sequence_id}: {conversation[:]}")
