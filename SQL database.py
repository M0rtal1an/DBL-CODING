import json
import sqlite3
import os

# assign directory

conn = sqlite3.connect(r"C:\Users\Usuario\Desktop\TUE\DBL- 1\airlines.db")
# Create a cursor object
cursor = conn.cursor()

    # Create a table for the tweets
cursor.execute('''CREATE TABLE IF NOT EXISTS 
                    (created_at TEXT, id INTEGER PRIMARY KEY, id_str TEXT, text TEXT,
                    source TEXT, truncated INTEGER, in_reply_to_status_id INTEGER,
                    in_reply_to_status_id_str TEXT, in_reply_to_user_id INTEGER,
                    in_reply_to_user_id_str TEXT, in_reply_to_screen_name TEXT, user_id INTEGER,
                    user_name TEXT, user_screen_name TEXT, user_location TEXT, user_description TEXT,
                    user_protected INTEGER, user_verified INTEGER, user_followers_count INTEGER,
                    user_friends_count INTEGER, user_listed_count INTEGER, user_favourites_count INTEGER,
                    user_statuses_count INTEGER, user_created_at TEXT, user_geo_enabled INTEGER,user_default_profile
                    BLOB, user_default_profile_image
                    BLOB, user_contributors_enabled INTEGER,
                    user_is_translator INTEGER, is_quote_status INTEGER, quote_count INTEGER,
                    reply_count INTEGER, retweet_count INTEGER, favorite_count INTEGER)''')

    # Insert the data into the table

directory = "C:/Users/Usuario/Desktop/TUE/DBL- 1/datax/data"  # Get the current working directory (cwd)
files = os.listdir(directory)  # Get all the files in that directory

for file in files:
    with open(f"C:/Users/Usuario/Desktop/TUE/DBL- 1/datax/data/{file}") as tweets:
        print(file)
        data = tweets.read()
        lines = data.split('\n')

        # Loop over each line and parse the JSON object
        objects = []
        for line in lines:
            # Skip any empty lines
            if not line:
                continue

            # Parse the JSON object
            obj = json.loads(line)

            # Append the object to the list
            objects.append(obj)
    # Print the list of objects


    for tweet in objects:
        try:
            user = tweet['user']
            cursor.execute(
                '''INSERT INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (tweet['created_at'], tweet['id'], tweet['id_str'], tweet['text'], tweet['source'], tweet['truncated'],
                 tweet['in_reply_to_status_id'], tweet['in_reply_to_status_id_str'], tweet['in_reply_to_user_id'],
                 tweet['in_reply_to_user_id_str'], tweet['in_reply_to_screen_name'], user['id'], user['name'],
                 user['screen_name'], user['location'], user['description'], user['protected'], user['verified'],
                 user['followers_count'], user['friends_count'], user['listed_count'], user['favourites_count'],
                 user['statuses_count'], user['created_at'], user['geo_enabled'],
                 user['default_profile'],
                 user['default_profile_image'], user['contributors_enabled'], user['is_translator'],
                 tweet['is_quote_status'],
                 tweet['quote_count'], tweet['reply_count'], tweet['retweet_count'], tweet['favorite_count']))
        except:
            continue

        conn.commit()

