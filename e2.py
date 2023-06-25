# Python学习
# 测试人：周晨骁
# 开发时间： 2023/6/23 19:56
import ast
import sqlite3
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Read the file
with open('time_conversations_verified.txt', 'r') as file:
    lines = file.readlines()

# Parse each line as a list and store in a list
list_of_lists = []
for line in lines:
    line = line.strip()
    try:
        list_of_lists.append(ast.literal_eval(line))
    except SyntaxError:
        print(f"Couldn't parse line: {line}")

# Convert the list of lists into a DataFrame
dataframe = pd.DataFrame(list_of_lists)
dataframe.fillna(0, inplace=True)

# Define a function to convert strings to datetime
def convert_to_datetime(x):
    if isinstance(x, str):
        # Remove extra spaces and single quotes
        x = x.strip().strip("'")
        return datetime.strptime(x, '%a %b %d %H:%M:%S +0000 %Y')
    else:
        return x

# Apply the function to the entire DataFrame
dataframe = dataframe.applymap(convert_to_datetime)

total_time = []
a=0
for i in range(0,24):
    time = dataframe[0][i]
    for j in range(2,22,2):
        if dataframe[j][i] == 0:
            break
        else:
            a+=1
            time += dataframe[j][i]-dataframe[j-1][i]
    total_time.append(time-dataframe[0][i])

total = total_time[0]
for i in range(0,len(total_time)):
    total += total_time[i]
mean_time_ver = total / a
print(mean_time_ver)


# Read the file
with open('date_conversations.txt', 'r') as file:
    lines = file.readlines()

# Parse each line as a list and store in a list
list_of_lists = []
for line in lines:
    line = line.strip()
    try:
        list_of_lists.append(ast.literal_eval(line))
    except SyntaxError:
        print(f"Couldn't parse line: {line}")

# Convert the list of lists into a DataFrame
dataframe = pd.DataFrame(list_of_lists)
dataframe.fillna(0, inplace=True)

# Define a function to convert strings to datetime
def convert_to_datetime(x):
    if isinstance(x, str):
        # Remove extra spaces and single quotes
        x = x.strip().strip("'")
        return datetime.strptime(x, '%a %b %d %H:%M:%S +0000 %Y')
    else:
        return x

# Apply the function to the entire DataFrame
dataframe = dataframe.applymap(convert_to_datetime)
print(dataframe)

total_time = []
a=0
for i in range(0,556):
    time = dataframe[0][i]
    for j in range(2,22,2):
        if dataframe[j][i] == 0:
            break
        else:
            a+=1
            time += dataframe[j][i]-dataframe[j-1][i]
    total_time.append(time-dataframe[0][i])

total = total_time[0]
for i in range(0,len(total_time)):
    total += total_time[i]
mean_time_nor = total / a
print(mean_time_nor)



# # Read the file
# with open('ordered_conversations1.txt', 'r') as file:
#     lines = file.readlines()
#
# # Parse each line as a list and store in a list
# list_of_lists = []
# for line in lines:
#     line = line.strip()
#     try:
#         list_of_lists.append(ast.literal_eval(line))
#     except SyntaxError:
#         print(f"Couldn't parse line: {line}")
#
# # Convert the list of lists into a DataFrame
# dataframe = pd.DataFrame(list_of_lists)
# dataframe.fillna(0, inplace=True)
#
# sentiment_change = []
# for i in range(0,500):
#     time = dataframe[0][i]
#     for j in range(1, 7):
#         if dataframe[j][i] == 0:
#             break
#         else:
#             time += dataframe[j][i] - dataframe[j-1][0]
#     sentiment_change.append(time-dataframe[0][i])
#
# print(sum(sentiment_change)/500)


# print(ver_total/a)
# print(nor_total/a)
# print(dataframe[2][0]-dataframe[1][0])
# print(len(total_time))

