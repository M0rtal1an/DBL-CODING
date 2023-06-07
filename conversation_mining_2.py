import sqlite3

conn = sqlite3.connect("C:/GIT DBL1/airlines.db")
cursor = conn.cursor()

og_tweets_airline_query = "SELECT id, CAST(in_reply_to_status_id as INTEGER), CAST(in_reply_to_user_id as INTEGER), user_id FROM data_new WHERE in_reply_to_user_id IS NULL AND user_id IN (45621423,218730857,18332190, 22536055, 124476322, 20626359, 106062176, 1542862735, 38676903, 253340062, 56377143)"
users_query = "SELECT id, CAST(in_reply_to_status_id as INTEGER), CAST(in_reply_to_user_id as INTEGER), user_id FROM data_new WHERE user_id NOT IN (45621423,218730857,18332190, 22536055, 124476322, 20626359, 106062176, 1542862735, 38676903, 253340062, 56377143) AND in_reply_to_user_id IS NOT NULL"
airlines_query = "SELECT id, CAST(in_reply_to_status_id as INTEGER), CAST(in_reply_to_user_id as INTEGER), user_id FROM data_new WHERE user_id IN (45621423,218730857,18332190, 22536055, 124476322, 20626359, 106062176, 1542862735, 38676903, 253340062, 56377143) AND in_reply_to_user_id IS NOT NULL"

og_airline_tweets = cursor.execute(og_tweets_airline_query).fetchall()
user_replies = cursor.execute(users_query).fetchall()
airlines_replies = cursor.execute(airlines_query).fetchall()

def get_conversation(user_id, replies):
    conversation = [(user_id,)]
    current_user_id = user_id
    while True:
        next_reply = None
        for reply in replies:
            if isinstance(conversation[-1], tuple) and reply[3] == current_user_id and reply[2] == conversation[0][0]:
                next_reply = reply
                break
        if next_reply is None:
            break
        conversation.append(next_reply)
        current_user_id = next_reply[3]
    print(conversation)
    return conversation

conversations = []

for og_tweet in og_airline_tweets:
    og_tweet_user_id = og_tweet[3]
    conversation = get_conversation(og_tweet_user_id, user_replies + airlines_replies)
    conversation_ids = [tweet[0] for tweet in conversation if isinstance(tweet, tuple)]
    conversations.append(conversation_ids)

print(conversations)
