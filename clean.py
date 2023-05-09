import numpy as np
import pandas as pd
import sqlite3
from geotext import GeoText


conn = sqlite3.connect('D:/Code/airlines.db')

data_query_Virgin_raw = """--sql
    SELECT id, created_at,in_reply_to_status_id, in_reply_to_user_id, in_reply_to_screen_name, user_id, user_name, user_followers_count, user_friends_count,user_favourites_count, user_created_at, user_location, user_verified, text, user_geo_enabled, user_default_profile, is_quote_status
    FROM tweets
    WHERE in_reply_to_user_id = 20626359 or user_id = 20626359
"""

data_Virgin_raw = pd.read_sql_query(data_query_Virgin_raw, conn)
data_Virgin_raw1 = data_Virgin_raw.dropna()
data_Virgin = data_Virgin_raw1.astype({'in_reply_to_user_id': int})



data_query_Lufthansa_raw = """--sql
    SELECT id, created_at,in_reply_to_status_id, in_reply_to_user_id, in_reply_to_screen_name, user_id, user_name, user_followers_count, user_friends_count,user_favourites_count, user_created_at, user_location, user_verified, text, user_geo_enabled, user_default_profile, is_quote_status
    FROM tweets
    WHERE in_reply_to_user_id = 20626359 or user_id = 20626359
"""

data_Lufthansa_raw = pd.read_sql_query(data_query_Lufthansa_raw, conn)
data_Lufthansa_raw1 = data_Lufthansa_raw.dropna()
data_Lufthansa = data_Lufthansa_raw1.astype({'in_reply_to_user_id': int})




data_query_others_raw = """--sql
    SELECT id, created_at,in_reply_to_status_id, in_reply_to_user_id, in_reply_to_screen_name, user_id, user_name, user_followers_count, user_friends_count,user_favourites_count, user_created_at, user_location, user_verified, text, user_geo_enabled, user_default_profile, is_quote_status
    FROM tweets
    WHERE in_reply_to_user_id = 18332190 or user_id = 18332190 or in_reply_to_user_id = 56377143 or user_id = 56377143 or in_reply_to_user_id = 106062176 or user_id = 106062176 or in_reply_to_user_id = 22536055 or user_id = 22536055 or in_reply_to_user_id = 26223583 or user_id = 26223583 or in_reply_to_user_id = 2182373406 or user_id = 2182373406 or in_reply_to_user_id = 38676903 or user_id = 38676903 or in_reply_to_user_id = 1542862735 or user_id = 1542862735 or in_reply_to_user_id = 253340062 or user_id = 253340062 or in_reply_to_user_id = 218730857 or user_id = 218730857 or in_reply_to_user_id = 45621423 or user_id = 45621423
"""

data_others_raw = pd.read_sql_query(data_query_others_raw, conn)
data_others_raw1 = data_others_raw.dropna()
data_others = data_others_raw1.astype({'in_reply_to_user_id': int})




data_query_others_raw = """--sql
    SELECT id, created_at, in_reply_to_user_id, in_reply_to_screen_name,
"""

print(data_Virgin)
print(data_Lufthansa)
print(data_others)



# print(data_KLM)
# print(data_France)
# print(data_America)
# print(data_Berlin)
# print(data_easyJet)
# print(data_RyanAir)
# print(data_Singapore)
# print(data_Qantas)
# print(data_EtihadAirways)
