import datetime
import ast
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

conversations_file_path = "C:/GIT DBL1/DBL-CODING/ordered_conversations.txt"

empty = []

with open(conversations_file_path, 'r') as file:
    lines = file.readlines()
text= []
for line in lines:
    text.append(line.strip().split(','))
sentiments=[]
text2 = [l for l in text if len(l)>9]
t= 0
for i in text2:
    sent = []
    k = i[2::3]
    for j in k:
        sent.append(j)
    sentiments.append(sent)
    result = [[value for value in sublist if value != ' None' and value != ' 0.0'] for sublist in sentiments]
    filtered_list = []
    for n in result:
        if n == empty:
            filtered_list.append([0])
        else:
            filtered_list.append(n)
    sentiment_changes = []

    for sents in filtered_list:
        sents = [float(i) for i in sents]
        sentiment_change = sents[-1] - sents[0]
        sentiment_changes.append(sentiment_change)

print(sorted(sentiment_changes))

conversations_file_path = "C:/GIT DBL1/DBL-CODING/date_conversations.txt"


# Read the file
with open(conversations_file_path, 'r') as file:
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

time_differences_min = [i/60 for i in average_time_difference]

# Define the interval size in minutes
interval_minutes = 15


# Filter out 0.0 sentiment changes and corresponding time differences
filtered_data = [(time, sentiment) for time, sentiment in zip(time_differences_min, sentiment_changes) if sentiment != 0.0 and time < 2000]

# Separate the filtered data into x and y lists
x = [entry[0] for entry in filtered_data]
y = [entry[1] for entry in filtered_data]

# Create bins based on the interval size
bins = np.arange(0, max(x) + interval_minutes, interval_minutes)

# Group the data into the bins
bin_indices = np.digitize(x, bins)

# Calculate the mean sentiment change for each bin
binned_data = {}
for i, index in enumerate(bin_indices):
    if index not in binned_data:
        binned_data[index] = []
    binned_data[index].append(y[i])

# Calculate the mean sentiment change and corresponding time for each bin
x_mean = []
y_mean = []
for index, values in binned_data.items():
    mean_time = np.mean([x[i] for i, bin_index in enumerate(bin_indices) if bin_index == index])
    mean_sentiment = np.mean(values)
    x_mean.append(mean_time)
    y_mean.append(mean_sentiment)

# Perform polynomial regression
degree = 2  # Specify the degree of the polynomial
poly_features = PolynomialFeatures(degree=degree)
x_poly = poly_features.fit_transform(np.array(x_mean).reshape(-1, 1))

poly_model = LinearRegression()
poly_model.fit(x_poly, y_mean)
poly_regression_line = poly_model.predict(x_poly)

# Sort the data for plotting
sorted_indices = np.argsort(x_mean)
sorted_x = np.array(x_mean)[sorted_indices]
sorted_y = np.array(y_mean)[sorted_indices]
sorted_poly_regression_line = np.array(poly_regression_line)[sorted_indices]

# Plot the scatter plot and polynomial regression line
plt.scatter(sorted_x, sorted_y)
plt.plot(sorted_x, sorted_poly_regression_line, color='red')
plt.xlabel('Time Differences (minutes)')
plt.ylabel('Mean Sentiment Change')
plt.title('How does response time affect sentiment change?')
plt.show()