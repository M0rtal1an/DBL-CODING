import sqlite3
from dateutil import parser


# Read conversations.txt file
conversations_file_path = r'C:\GIT DBL1\DBL-CODING\new_conversations.txt'

with open(conversations_file_path, 'r') as file:
    lines = file.readlines()


# Extract tweet IDs from each line
tweet_ids = []
for line in lines:
    sequence = line.strip().split(' ')
    tweet_ids.append(sequence)

# Connect to the database
database_path = r'C:\GIT DBL1\airlines.db'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# Retrieve conversations from the database based on tweet IDs
conversations = []
for conversation in tweet_ids:
    convo = []
    for tweet_id in conversation:
        pair = cursor.execute("SELECT id, created_at, sentiment_score, user_verified FROM data_new WHERE id = ?", (tweet_id,))
        result = pair.fetchall()
        convo.extend(result)
    sorted_conversation = sorted(convo, key=lambda x: parser.parse(x[1]))
    print(sorted_conversation)
    if sorted_conversation[1][3] == 0:
        conversations.append(sorted_conversation)


# Save the organized conversations to a new text file
output_file_path = r'C:\GIT DBL1\DBL-CODING\time_conversations_non_verified.txt'
with open(output_file_path, 'w') as output_file:
    for conversation in conversations:
        dates = [item[1] for item in conversation]
        dates_str = ",".join(dates)
        output_file.write(dates_str)
        output_file.write('\n')

# Close the database connection
connection.close()
