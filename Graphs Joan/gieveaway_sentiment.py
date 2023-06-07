
import datetime
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('C:/GIT DBL1/airlines.db')
cursor = conn.cursor()

replies_query = "SELECT id, created_at, sentiment_score FROM data_new WHERE in_reply_to_user_id == 1542862735 AND user_id != 1542862735"
giveaways_query = "SELECT id, created_at FROM data_new WHERE id IN (1133680257188413440, 1139109906789912577, 1173541976718925825, 1198903662447398912, 1209034371296059393, 1219234028253065216, 1227895437975310342)"

giveaways = cursor.execute(giveaways_query).fetchall()
user_replies = cursor.execute(replies_query).fetchall()

important_tweets = []
replies = []

# Convert giveaway tweets to important_tweets format
for giveaway in giveaways:
    tweet_id = giveaway[0]
    created_at = giveaway[1]
    sentiment_score = None  # Modify this if sentiment score is available in the giveaways table

    important_tweets.append({
        'id': tweet_id,
        'created_at': created_at,
        'sentiment_score': sentiment_score
    })

# Convert user replies to replies format
for reply in user_replies:
    reply_id = reply[0]
    created_at = reply[1]
    sentiment_score = reply[2]

    replies.append({
        'id': reply_id,
        'created_at': created_at,
        'sentiment_score': sentiment_score
    })

# Rest of the code remains the same

hourly_sentiment_scores = []

for tweet in important_tweets:
    tweet_time = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
    start_time = tweet_time - datetime.timedelta(days=2)
    end_time = tweet_time + datetime.timedelta(days=2)

    hourly_scores = [0] * 97  # 97 values for 97 hours (24 hours x 2 + 1 hour)

    for reply in replies:
        reply_time = datetime.datetime.strptime(reply['created_at'], '%a %b %d %H:%M:%S %z %Y')

        if start_time <= reply_time <= end_time:
            hour_diff = (reply_time - start_time).total_seconds() // 3600
            hourly_scores[int(hour_diff)] += reply['sentiment_score']

    hourly_sentiment_scores.append(hourly_scores)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Generate plots
for i, scores in enumerate(hourly_sentiment_scores):
    hours = list(range(-48, 49))
    ax.plot(hours, scores, label=f"Tweet {i+1}")

# Set plot title and labels
ax.set_title("Sentiment Scores for Important Tweets")
ax.set_xlabel("Hours")
ax.set_ylabel("Sentiment Score")

# Set X-axis ticks
ax.set_xticks(list(range(-48, 49, 12)))
ax.set_xticklabels(list(range(-48, 49, 12)))


plt.show()