import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\airlines_sentiment.db")

# Create a cursor
cur = conn.cursor()

# Execute the SQL query to fetch the required data
cur.execute("SELECT created_at, sentiment_score FROM data_new")

# Fetch all the rows as a list of tuples
rows = cur.fetchall()

# Create a Pandas DataFrame from the rows
df = pd.DataFrame(rows, columns=["created_at", "sentiment_score"])

# Convert the 'created_at' column to datetime format
df['created_at'] = df['created_at'].apply(lambda x: datetime.strptime(x, "%a %b %d %H:%M:%S %z %Y"))

# Extract the day of the week and hour from the 'created_at' column
df['day_of_week'] = df['created_at'].dt.day_name()
df['hour'] = df['created_at'].dt.hour

# Create a pivot table to aggregate sentiment scores by day of the week and hour
pivot_table = df.pivot_table(index='hour', columns='day_of_week', values='sentiment_score', aggfunc='mean')

# Define the order of weekdays for proper sorting on the heatmap
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt=".2f", cbar=True, linewidths=0.5, yticklabels=range(0, 24), xticklabels=weekday_order)

# Set the title and labels
plt.title("Sentiment Scores by Time of Day and Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Hour of Day")

# Display the heatmap
plt.show()

# Close the cursor
cur.close()

# Close the connection
conn.close()
