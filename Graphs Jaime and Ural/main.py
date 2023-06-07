import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\cleanairlines.db")
# create a cursor
cur = conn.cursor()
airlines_list = ['British Airways','American Airlines', 'Virgin Atlantic', 'Lufthansa', 'easyJet', 'Ryanair', 'Royal Dutch Airlines', 'Air France']
tweet_counts = {}
for airline in airlines_list:
    number_of_tweets = f"""--sql
        SELECT count(user_name)
        FROM data_new
        WHERE user_name = '{airline}'
    """
    # execute the query
    cur.execute(number_of_tweets)

    # fetch the results
    result = cur.fetchone()[0]

    # print the result
    print(f"{airline} has tweeted {result} times.")
    tweet_counts[airline] = result
    # create a dataframe from the tweet_counts dictionary
df = pd.DataFrame.from_dict(tweet_counts, orient='index', columns=['tweet_count'])

# add a column for the airline name
df['Airline'] = df.index

# reset the index of the dataframe
df.reset_index(drop=True, inplace=True)
df = df.set_index('Airline')

# display the dataframe
print(df)

ax = df.plot.bar(  y='tweet_count', legend=False, figsize =(10,9))

# set the title and labels
ax.set_title("Number of Tweets by Airline")
ax.set_xlabel("Airline")
ax.set_ylabel("Number of Tweets")
plt.subplots_adjust(bottom=0.2)
plt.xticks(rotation=35)
plt.show()









