# WOrking with CSV Data and Pandas Library


import csv

# with open("Day_25/day-25-start/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         #print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))    
        
#     print(temperatures)


import pandas




# print(data)
# for temp in data["temp"]:
#     1

# print(sum)
# print(data["temp"].mean())
# print(data.temp)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp *= 9/5 + 32
# print(monday_temp)

data = pandas.DataFrame()
data = pandas.read_csv("Day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)