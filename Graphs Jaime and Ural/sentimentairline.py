import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\airlines_sentiment.db")

# Create a cursor
cur = conn.cursor()

# Define the airlines list
airlines_list = ['British Airways', 'American Airlines', 'Virgin Atlantic', 'Lufthansa', 'easyJet', 'Ryanair', 'KLM', 'Air France']
airlines_list_id = [18332190.0, 22536055.0, 20626359.0, 124476322.0, 38676903.0, 1542862735.0, 56377143.0, 106062176.0]

# Initialize a dictionary to store the sentiment counts for each airline
sentiment_counts = {
    "negative": [],
    "neutral": [],
    "positive": []
}

# Loop through the airlines list
for airline in airlines_list_id:
    # Execute the SQL query to get the sentiment analysis scores for the replies to tweets by the current airline
    cur.execute(f"SELECT sentiment_score FROM data_new WHERE in_reply_to_user_id = '{airline}'")

    # Fetch all the sentiment analysis scores as a list of tuples
    rows = cur.fetchall()

    # Create a Pandas DataFrame from the sentiment analysis scores
    df = pd.DataFrame(rows, columns=["sentiment_analysis"])

    # Categorize the sentiment scores
    df["sentiment_category"] = pd.cut(df["sentiment_analysis"], bins=[-1, -0.2, 0.2, 1], labels=["negative", "neutral", "positive"])

    # Count the number of tweets in each sentiment category
    sentiment_counts["negative"].append(df[df["sentiment_category"] == "negative"].shape[0])
    sentiment_counts["neutral"].append(df[df["sentiment_category"] == "neutral"].shape[0])
    sentiment_counts["positive"].append(df[df["sentiment_category"] == "positive"].shape[0])

# Create a DataFrame from the sentiment_counts dictionary
df_sentiment = pd.DataFrame(sentiment_counts, index=airlines_list)

# Get the number of sentiment categories
num_sentiment_categories = len(sentiment_counts)

# Set the width of each bar
bar_width = 0.2

# Calculate the x positions for the bars
x = np.arange(len(airlines_list))

# Create a grouped bar chart
fig, ax = plt.subplots()
for i, sentiment_category in enumerate(sentiment_counts.keys()):
    ax.bar(x + i * bar_width, df_sentiment[sentiment_category], width=bar_width, label=sentiment_category)

# Set the x-axis ticks and labels
ax.set_xticks(x + (num_sentiment_categories - 1) * bar_width / 2)
ax.set_xticklabels(airlines_list)

# Set the title and labels
ax.set_title("Sentiment Analysis of Replies to Tweets by Airline")
ax.set_xlabel("Airline")
ax.set_ylabel("Number of Replies")

# Add a legend
ax.legend()

# Display the chart
plt.subplots_adjust(top = 0.9, bottom = 0.25)
plt.xticks(rotation=35)
plt.show()




