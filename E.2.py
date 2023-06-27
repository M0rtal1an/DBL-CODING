# Python学习
# 测试人：周晨骁
# 开发时间： 2023/6/21 16:09
import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('D:/tem/DBL-CODING/airlines.db')

# user_verified, sentiment_score,
data_query_verified_positive = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 1 and sentiment_score >= 0 
"""

data_query_verified_positive1 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 1 and  sentiment_score >= -1 and sentiment_score < -0.6
"""

data_query_verified_positive2 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 1 and sentiment_score >= -0.6 and sentiment_score < -0.2
"""

data_query_verified_positive3 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 1 and sentiment_score >= -0.2 and sentiment_score < 0.2
"""

data_query_verified_positive4 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 1 and sentiment_score >= 0.2 and sentiment_score < 0.6
"""

data_query_verified_positive5 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 1 and sentiment_score >= 0.6 and sentiment_score < 1
"""

data_query_verified_negative = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 1 and sentiment_score < 0 
"""


data_query_normal1 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 0 and  sentiment_score >= -1 and sentiment_score < -0.6
"""

data_query_normal2 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 0 and sentiment_score >= -0.6 and sentiment_score < -0.2
"""

data_query_normal3 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 0 and sentiment_score >= -0.2 and sentiment_score < 0.2
"""

data_query_normal4 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 0 and sentiment_score >= 0.2 and sentiment_score < 0.6
"""

data_query_normal5 = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 0 and sentiment_score >= 0.6 and sentiment_score < 1
"""


data_query_normal_positive = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 0 and sentiment_score >= 0 
"""

data_query_normal_negative = """--sql
    SELECT count(user_verified), avg(sentiment_score)
    From data_new
    Where user_verified = 0 and sentiment_score < 0 
"""


data_v_p = pd.read_sql_query(data_query_verified_positive, conn)
data_raw1 = data_v_p.dropna()
data_v_n = pd.read_sql_query(data_query_verified_negative, conn)
data_raw2 = data_v_n.dropna()

# verified distribution
data_v_p1 = pd.read_sql_query(data_query_verified_positive1, conn)
data_raw11 = data_v_p1.dropna()
data_v_p2 = pd.read_sql_query(data_query_verified_positive2, conn)
data_raw12 = data_v_p2.dropna()
data_v_p3 = pd.read_sql_query(data_query_verified_positive3, conn)
data_raw13 = data_v_p3.dropna()
data_v_p4 = pd.read_sql_query(data_query_verified_positive4, conn)
data_raw14 = data_v_p4.dropna()
data_v_p5 = pd.read_sql_query(data_query_verified_positive5, conn)
data_raw15 = data_v_p5.dropna()



data_v_n = pd.read_sql_query(data_query_normal_positive, conn)
data_raw3 = data_v_n.dropna()
data_v_n = pd.read_sql_query(data_query_normal_negative, conn)
data_raw4 = data_v_n.dropna()


# normal distribution
data_v_n1 = pd.read_sql_query(data_query_normal1, conn)
data_raw31 = data_v_n1.dropna()
data_v_n2 = pd.read_sql_query(data_query_normal2, conn)
data_raw32 = data_v_n2.dropna()
data_v_n3 = pd.read_sql_query(data_query_normal3, conn)
data_raw33 = data_v_n3.dropna()
data_v_n4 = pd.read_sql_query(data_query_normal4, conn)
data_raw34 = data_v_n4.dropna()
data_v_n5 = pd.read_sql_query(ddata_query_normal5, conn)
data_raw35 = data_v_n5.dropna()



print(data_raw1)
print(data_raw2)
# print(data_raw11)
# print(data_raw12)
# print(data_raw13)
# print(data_raw14)
# print(data_raw15)

print(data_raw3)
print(data_raw4)
# print(data_raw31)
# print(data_raw32)
# print(data_raw33)
# print(data_raw34)
# print(data_raw35)