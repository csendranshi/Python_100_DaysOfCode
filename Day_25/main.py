# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1]!= 'temp':
#             temperatures.append(int(row[1]))
#         # print(row)
#         print(temperatures)

import pandas as pd

data = pd.read_csv('weather_data.csv')
print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

data_list = data["temp"].tolist()
print(data_list)

print(f"The Average Temperature is {sum(data_list)/len(data_list)}")

print(data["temp"].mean())
max_temp = data["temp"].max()
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)

# create dataframe from scratch
data_dict = {
    "students":["Amy","Jamie","Anshika"],
    "scores":[75,25,98]
}
new_df = pd.DataFrame(data_dict)
print(new_df)
new_df.to_csv("newdata.csv")