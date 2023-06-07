import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\cleanairlines.db")
cur = conn.cursor()

# Get all the tweet data and times
cur.execute("SELECT text, created_at FROM data_new")
rows = cur.fetchall()

# Create a dictionary to store the counts for each hour
counts = {}
for i in range(24):
    counts[i] = 0

# Loop through each row and count the tweets for each hour
for row in rows:
    tweet_time = row[1]  # get the time of the tweet
    hour = int(tweet_time[11:13])  # extract the hour from the time string
    counts[hour] += 1  # add 1 to the count for that hour

# Print out the counts for each hour
for hour, count in counts.items():
    print(f"Tweets at hour {hour}: {count}")


# create a DataFrame from the counts dictionary
df = pd.DataFrame.from_dict(counts, orient='index', columns=['tweet_count'])

# add a column for the hour of the day
df['hour_of_day'] = df.index

# display the DataFrame
print(df)
ax = df['tweet_count'].plot()
ax.set_title("Number of Tweets by Hour")
ax.set_xlabel("Time (24h)")
ax.set_ylabel("Number of Tweets");
plt.show()