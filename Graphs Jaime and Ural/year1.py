
import sqlite3
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\airlines_sentiment.db")

# create a cursor
cur = conn.cursor()

# query to get all tweets and their dates
query = "SELECT text, created_at FROM data_new"

# execute the query
cur.execute(query)

# create a dictionary to store tweet counts for each day of the year
tweet_counts = {}
for i in range(1, 367):
    tweet_counts[i] = 0

# loop through the tweets and count the number of tweets for each day of the year
for row in cur.fetchall():
    # extract the date from the tweet
    date_str = row[1][4:10] + " " + row[1][-4:]
    date = datetime.strptime(date_str, "%b %d %Y")  # parse the date string as datetime object

    # increment the tweet count for the corresponding day of the year
    tweet_counts[date.timetuple().tm_yday] += 1

# print the tweet counts for each day of the year
for day, count in tweet_counts.items():
    print(f"Day {day}: {count} tweets")

# create a DataFrame from the tweet_counts dictionary
df = pd.DataFrame.from_dict(tweet_counts, orient='index', columns=['tweet_count'])

# add a column for the day of the year
df['day_of_year'] = df.index

# display the DataFrame
print(df)

ax = df['tweet_count'].plot()
ax.set_title("Number of Tweets by Day of Year")
ax.set_xlabel("Day of the year")
ax.set_ylabel("Number of Tweets");

plt.show()

