import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\airlines_sentiment.db")

# Create a cursor
cur = conn.cursor()

# Execute the SQL query to get the data for the specified timeframe
cur.execute("SELECT created_at, user_verified, sentiment_score FROM data_new ")

# Fetch all the rows as a list of tuples
rows = cur.fetchall()

# Create a Pandas DataFrame from the rows
df = pd.DataFrame(rows, columns=["created_at", "user_verified", "sentiment_score"])

# Convert the 'sentiment_score' column to numeric type
df['sentiment_score'] = pd.to_numeric(df['sentiment_score'], errors='coerce')

# Convert the 'created_at' column to datetime format
df['created_at'] = df['created_at'].apply(lambda x: datetime.strptime(x, "%a %b %d %H:%M:%S %z %Y"))

# Extract the month and year from the 'created_at' column
df['month_year'] = df['created_at'].dt.to_period('M')

# Group the data by 'month_year' and 'user_verified', and calculate the mean sentiment score
df_grouped = df.groupby(['month_year', 'user_verified']).mean().reset_index()

# Pivot the DataFrame to have 'user_verified' as columns and 'month_year' as index
df_pivot = df_grouped.pivot(index='month_year', columns='user_verified', values='sentiment_score')

# Create a line graph
ax = df_pivot.plot(kind='line', marker='o')

# Set the title and labels
ax.set_title('Mean Sentiment Values Over Months')
ax.set_xlabel('Month')
ax.set_ylabel('Mean Sentiment Value')

# Update the legend labels
legend_labels = ['Not Verified', 'Verified']
ax.legend(legend_labels, title='User Type')
plt.subplots_adjust(top = 0.9, bottom = 0.15)

# Display the graph
plt.show()


