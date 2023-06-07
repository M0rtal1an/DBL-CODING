import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to the database
conn = sqlite3.connect(r"C:\Users\20221619\PycharmProjects\pythonProject1\cleanairlines.db")

# create a cursor
cur = conn.cursor()

# define the list of airlines to include in the graph
airlines_list = ['British_Airways', 'AmericanAir', 'VirginAtlantic', 'lufthansa', 'easyJet', 'Ryanair', 'KLM', 'airfrance']

# create a dictionary to store the tweet counts for each airline and user type
data = {'Airline': [], 'Verified': [], 'Non-Verified': []}

# loop through each airline and execute the queries
for airline in airlines_list:
    # query the number of tweets from verified users
    query_verified = f"SELECT COUNT(*) FROM data_new WHERE in_reply_to_screen_name = '{airline}' AND user_verified = 1"
    cur.execute(query_verified)
    count_verified = cur.fetchone()[0]

    # query the number of tweets from non-verified users
    query_non_verified = f"SELECT COUNT(*) FROM data_new WHERE in_reply_to_screen_name = '{airline}' AND user_verified = 0"
    cur.execute(query_non_verified)
    count_non_verified = cur.fetchone()[0]

    # add the results to the data dictionary
    data['Airline'].append(airline)
    data['Verified'].append(count_verified)
    data['Non-Verified'].append(count_non_verified)

# create a pandas dataframe from the data dictionary
df = pd.DataFrame(data)

# set the airline column as the index
df.set_index('Airline', inplace=True)

print(df)

# create the dataframe
data = {'Airline': ['British_Airways', 'AmericanAir', 'VirginAtlantic', 'lufthansa', 'easyJet', 'Ryanair', 'KLM', 'AirFrance'],
        'Verified': [1548, 3459, 511, 303, 608, 395, 511, 0],
        'Non-Verified': [146339, 169152, 31675, 22857, 100005, 90854, 48455, 0]}
df = pd.DataFrame(data)
df.set_index('Airline', inplace=True)

# calculate the ratios of verified to non-verified tweets
df['Ratio'] = df['Verified'] / df['Non-Verified']
df.sort_values('Ratio', inplace=True)
# create the scatter plot
plt.scatter(df.index, df['Ratio'], s=100, alpha=0.5)

# set the x-axis label
plt.xlabel('Airline')

# set the y-axis label
plt.ylabel('Ratio %')

# set the title
plt.title('Ratio of Verified to Non-Verified Tweets Received by Airline')

# rotate the x-axis labels
plt.subplots_adjust(bottom=0.25)
plt.xticks(rotation=35)
plt.show()
# show the plot
plt.show()





