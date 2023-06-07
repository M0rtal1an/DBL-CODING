
import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


# connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\cleanairlines.db")

# create a cursor
cur = conn.cursor()

# execute the SQL query to get the data for all airlines
cur.execute("""
SELECT user_name, user_followers_count, COUNT(*) AS tweet_count
FROM data_new
WHERE user_name IN ('British Airways', 'American Airlines', 'Virgin Atlantic', 'Lufthansa', 'easyJet', 'Ryanair', 'Royal Dutch Airlines', 'Air France')
GROUP BY user_name
""")

# fetch all the rows as a list of tuples
rows = cur.fetchall()

# create a Pandas DataFrame from the rows
df = pd.DataFrame(rows, columns=["Airline", "Followers (Millions)", "Number of Tweets"])
print(df)

# create a scatter plot with regression line using seaborn
sns.lmplot(x="Followers (Millions)", y="Number of Tweets", data=df)
plt.title('Num of Followers vs Num of tweets per airline')
plt.subplots_adjust(top = 0.9, bottom = 0.1)
plt.show()