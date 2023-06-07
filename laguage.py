import sqlite3
from langdetect import detect
import pandas as pd
import matplotlib.pyplot as plt
# connect to the database
conn = sqlite3.connect(r"C:\GIT DBL1\airlines.db")

# create a cursor
cur = conn.cursor()

all_tweets="""--sql
        SELECT text
        FROM data_new
    """
# select all tweets from the table
cur.execute(all_tweets)

# fetch all the tweet texts
tweets = cur.fetchall()

# create a dictionary to store the count of tweets in each language
lang_counts = {}

# detect the language of each tweet text
i=1
for tweet in tweets:
    print(i)
    i+=1
    try:

        lang = detect(tweet[0])
        if lang in lang_counts:
            lang_counts[lang] += 1
        else:
            lang_counts[lang] = 1
    except:
        pass

# print the count of tweets in each language
for lang, count in lang_counts.items():
    print(f"{lang} language: {count} tweets")


# create a pandas dataframe from the lang_counts dictionary
df = pd.DataFrame.from_dict(lang_counts, orient='index', columns=['count'])

# sort the dataframe by count in descending order and select the top 5 languages
top_langs = df.sort_values(by='count', ascending=False).head(5)

# create a bar chart with the top 5 languages
ax = top_langs.plot.bar(rot=0, figsize=(10, 6))

# set the title and labels
ax.set_title("Top 5 Most Spoken Languages")
ax.set_xlabel("Language")
ax.set_ylabel("Number of Tweets")

# display the bar chart
plt.show()




