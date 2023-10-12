# import pickle
import datetime
import os

list_test = [datetime.datetime.now()]

# Specify the file path within the data folder in the GitHub workspace
file_path = 'test_data.txt'

with open(file_path, 'a') as file:
    for item in list_test:
        file.write(str(item) + "\n")

# print(list_test)
