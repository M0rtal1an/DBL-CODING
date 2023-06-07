import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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
    cur.execute(f"SELECT created_at, sentiment_score FROM data_new WHERE in_reply_to_user_id = '{airline_id}'")

    # Fetch all the sentiment analysis scores as a list of tuples
    rows = cur.fetchall()

    # Create a Pandas DataFrame from the sentiment analysis scores
    df = pd.DataFrame(rows, columns=["created_at", "sentiment_score"])

    # Convert the 'created_at' column to datetime format
    df['created_at'] = df['created_at'].apply(lambda x: datetime.strptime(x, "%a %b %d %H:%M:%S %z %Y"))

    # Group the data by month and calculate the mean sentiment score
    df_grouped = df.groupby(df['created_at'].dt.to_period('M'))['sentiment_score'].mean()

    # Store the mean sentiment scores in the dictionary
    mean_sentiment_scores[airline] = df_grouped

# Create a DataFrame from the mean_sentiment_scores dictionary
df_sentiment = pd.DataFrame(mean_sentiment_scores)

# Plot the line graph
ax = df_sentiment.plot(kind='line', marker='o')

# Set the title and labels
ax.set_title("Mean Sentiments Over Time for Each Airline")
ax.set_xlabel("Month")
ax.set_ylabel("Mean Sentiment Score")

# Add a legend
ax.legend(bbox_to_anchor=(1.05, 1))


# Display the chart
plt.show()

# Close the cursor
cur.close()

# Close the connection
conn.close()
