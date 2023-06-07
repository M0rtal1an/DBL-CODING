import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\airlines_sentiment.db")

# Create a cursor
cur = conn.cursor()

# Define the airlines list
airlines_list = ['British Airways', 'American Airlines', 'Virgin Atlantic', 'Lufthansa', 'easyJet', 'Ryanair', 'KLM', 'Air France']
airlines_list_id = [18332190.0, 22536055.0, 20626359.0, 124476322.0, 38676903.0, 1542862735.0, 56377143.0, 106062176.0]

# Initialize a dictionary to store the mean sentiment scores for each airline
mean_sentiment_scores = {}

# Loop through the airlines list
for airline, airline_id in zip(airlines_list, airlines_list_id):
    # Execute the SQL query to get the sentiment analysis scores for the replies to tweets by the current airline
    cur.execute(f"SELECT sentiment_score FROM data_new WHERE in_reply_to_user_id = '{airline_id}'")

    # Fetch all the sentiment analysis scores as a list of tuples
    rows = cur.fetchall()

    # Create a Pandas DataFrame from the sentiment analysis scores
    df = pd.DataFrame(rows, columns=["sentiment_score"])

    # Calculate the mean sentiment score
    mean_sentiment_score = df["sentiment_score"].mean()

    # Store the mean sentiment score in the dictionary
    mean_sentiment_scores[airline] = mean_sentiment_score

# Create a DataFrame from the mean_sentiment_scores dictionary
df_sentiment = pd.DataFrame.from_dict(mean_sentiment_scores, orient='index', columns=['mean_sentiment_score'])
df_sentiment.sort_values('mean_sentiment_score', inplace=True)

# Create a bar chart
ax = df_sentiment.plot(kind='bar', legend=False)

# Set the title and labels
ax.set_title("Mean Sentiment Analysis of Each Airline")
ax.set_xlabel("Airline")
ax.set_ylabel("Mean Sentiment Score")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()

# Close the cursor
cur.close()

# Close the connection
conn.close()
