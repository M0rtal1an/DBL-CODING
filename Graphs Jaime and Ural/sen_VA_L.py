import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to the database
conn = sqlite3.connect(r'C:\Users\20221619\PycharmProjects\pythonProject1\airlines_sentiment.db')

# Create a cursor
cur = conn.cursor()

# Execute the SQL query to get the data for the specified timeframe
cur.execute("SELECT created_at, user_verified, sentiment_score, in_reply_to_user_id FROM data_new WHERE in_reply_to_user_id IN (20626359, 124476322)")

# Fetch all the rows as a list of tuples
rows = cur.fetchall()

# Create a Pandas DataFrame from the rows
df = pd.DataFrame(rows, columns=["created_at", "user_verified", "sentiment_score", "in_reply_to_user_id"])

# Convert the 'sentiment_score' column to numeric type
df['sentiment_score'] = pd.to_numeric(df['sentiment_score'], errors='coerce')

# Convert the 'created_at' column to datetime format
df['created_at'] = df['created_at'].apply(lambda x: datetime.strptime(x, "%a %b %d %H:%M:%S %z %Y"))

# Extract the month and year from the 'created_at' column
df['month_year'] = df['created_at'].dt.to_period('M')

# Create a mapping dictionary for the legends
legend_mapping = {
    (20626359, 1): "Virgin Atlantic Verified",
    (20626359, 0): "Virgin Atlantic Not Verified",
    (124476322, 1): "Lutftansa Verified",
    (124476322, 0): "Lufthansa Not Verified"
}

# Group the data by 'month_year', 'in_reply_to_user_id', and 'user_verified', and calculate the mean sentiment score
df_grouped = df.groupby(['month_year', 'in_reply_to_user_id', 'user_verified']).mean().reset_index()

# Pivot the DataFrame to have 'in_reply_to_user_id' as columns, 'month_year' as index, and 'user_verified' as sub-columns
df_pivot = df_grouped.pivot(index='month_year', columns=['in_reply_to_user_id', 'user_verified'], values='sentiment_score')

# Create a line graph
ax = df_pivot.plot(kind='line', marker='o')

# Set the title and labels
ax.set_title('Mean Sentiment Values Over Months')
ax.set_xlabel('Month')
ax.set_ylabel('Mean Sentiment Value')

# Update the legend labels using the mapping dictionary
legend_labels = [legend_mapping.get((col[0], col[1]), "") for col in df_pivot.columns]
legend = ax.legend(title=['In Reply To User ID', 'User Type'], labels=legend_labels)

# Place the legend outside the graph
ax.legend(title="Legend:", labels=legend_labels, bbox_to_anchor=(1.05, 1))
plt.subplots_adjust(top = 0.9, bottom = 0.25, right =0.6)
# Display the graph
plt.show()

