import pandas as pd

data_file = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_sq = len(data_file[data_file["Primary Fur Color"] == "Gray"])
red_sq = len(data_file[data_file["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data_file[data_file["Primary Fur Color"] == "Black"])
print(grey_sq)
print(red_sq)
print(black_sq)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_sq,red_sq,black_sq]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")