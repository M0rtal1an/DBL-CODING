import sqlite3
import numpy as np
import matplotlib.pyplot as plt

database_path = "C:/GIT DBL1/airlines.db"
connection = sqlite3.connect(database_path)
cursor = connection.cursor()
user_tweets = cursor.execute("SELECT id FROM data_new WHERE user_id NOT IN (45621423,218730857,18332190, 22536055, 124476322, 20626359, 106062176, 1542862735, 38676903, 253340062) AND user_verified == 1").fetchall()

verified_tweets = [tweet[0] for tweet in user_tweets]

conversations_file_path = "C:/GIT DBL1/DBL-CODING/ordered_conversations.txt"

with open(conversations_file_path, 'r') as file:
    lines = file.readlines()

airlines = ['British Airways', 'American Airlines', 'Virgin Atlantic', 'Lufthansa', 'easyJet', 'Ryanair', 'Royal Dutch Airlines']
conversations = []
convos = []
for line in lines:
    convos.append(line.strip().split(','))

middle_means = []
upper_means = []
lower_means = []

for airline in airlines:
    conversations = []
    print(airline)
    airline_tweets = cursor.execute("SELECT id FROM data_new WHERE user_name == ?", (airline,)).fetchall()
    airline_tweet_ids = [tweet[0] for tweet in airline_tweets]

    for pot_convo in convos:
        if int(pot_convo[0]) in airline_tweet_ids:
            conversations.append(pot_convo)

    sentiments = []
    for i in conversations:
        if len(i) > 9:
            sent = []
            for j in i[2::3]:
                sent.append(j)
                sentiments.append(sent)

    result = [[value for value in sublist if value != ' None' and value != ' 0.0'] for sublist in sentiments]
    filtered_list = [lst for lst in result if lst]

    sent_changes = []
    upper = []
    last = []
    middle = []

    for sents in filtered_list:
        sent_diff = float(sents[-1]) - float(sents[0])
        sent_changes.append(sent_diff)
        upper.append(float(sents[0]))
        last.append(float(sents[-1]))
        middle.append((sents[1:-1]))

    non_empty_list = list(filter(lambda sub_list: sub_list, middle))
    difference_list = [x for x in sent_changes if x != 0]
    flat_data = [float(value) for sublist in middle for value in sublist if sublist]

    # Calculate the mean using numpy
    middle_mean = np.mean(flat_data)
    upper_mean = np.mean(upper)
    lower_mean = np.mean(last)
    middle_means.append(middle_mean)
    upper_means.append(upper_mean)
    lower_means.append(lower_mean)
    print(np.mean(difference_list))
    print(np.var(difference_list))

connection.close()

# Plotting the graph
categories = ['Start', 'Middle', 'End']
x = np.arange(len(categories))

for i, airline in enumerate(airlines):
    means = [upper_means[i], middle_means[i], lower_means[i]]
    plt.plot(x, means, label=airline)

plt.xticks(x, categories)
plt.xlabel('Categories')
plt.ylabel('Mean Values')
plt.title('Average sentiment change over conversation')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()