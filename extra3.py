import ast
import sqlite3
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

conversations_file_path = r'D:\Code\DBL-CODING-main\DBL-CODING-main\date_conversations.txt'


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




# Define a function to calculate the time difference between two columns
def calculate_time_difference(row, col1, col2):
    if isinstance(row[col1], datetime) and isinstance(row[col2], datetime):
        return (row[col2] - row[col1]).total_seconds()
    elif isinstance(row[col1], int) and isinstance(row[col2], int):
        return row[col2] - row[col1]
    else:
        return 0

# Calculate the time difference for each pair of columns
time_differences = []
for i in range(1, 20, 2):
    time_difference = dataframe.apply(calculate_time_difference, args=(i, i+1), axis=1)
    time_differences.append(time_difference)

# Convert the list of time differences into a DataFrame
time_differences_df = pd.DataFrame(time_differences).transpose()

# Calculate the average time difference for each row
average_time_difference = time_differences_df.mean(axis=1)
# Convert the average time difference from seconds to minutes
average_time_difference_in_minutes = average_time_difference / 60

average_time_difference_in_minutes = average_time_difference_in_minutes.tolist()
print(average_time_difference_in_minutes)

#print(average_time_difference_in_minutes)