# # TODO: Open up the weather_data.csv file and reading each line into a list
#
# with open("weather_data.csv") as weather_data:
#     #readline takes each lines and reads as an object in the list
#     data = weather_data.readlines()
#     print(data)

import csv



with open("weather_data.csv") as csvfile:
    data = csv.reader(csvfile)

    temp = []

    for row in data:
        # printing all temperatures
        # print(row[1])
        # To exclude columns name, print values as long as the value != 'temp'
        if row[1] != "temp":
            temp.append(int(row[1]))
    print(temp)

import pandas as pd
data = pd.read_csv("weather_data.csv")
# print(data["temp"])

#converting the data to a dictionary
data_dict = data.to_dict()
print(data_dict)

# converting data series(columns) into a python list
temp_list = data["temp"].tolist()
print(temp_list)

# TODO: Get the average temperature

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

print(data['temp'].mean())

print(data['temp'].max())

print(data['temp'].min())

print(data.condition)

# Getting row data where day is Monday
"""
    First, get the data we're working with. in this case 'data'
    then access the precise column for days, as data.days or data['days']
    then use the comparison operator to find the exact value you're searching for
    data[data.days == 'Monday']
"""
print("Getting row data where day is Monday \n")
print(data[data.day == "Monday"], '\n')

# Which row of data where temp was at max?
print("Which row of data where temp was at max? \n")
print(data[data.temp == data.temp.max()], '\n')

# But what if we wanted the row's day or condition
monday = data[data.day == "Monday"]
#tapping the other columns
print(monday.condition)

# Temp in Fahrenheit
mon_temp_fah = ((monday['temp']) * 1.8) + 32
print(mon_temp_fah)

"""
     OR
     monday = data[data.day == "Monday"]
     monday_temp = monday.temp[0]
     monday_temp_Fah = monday_temp * 9/5 + 32
     print(monday_temp_Fah)
"""

# Creating dataframes
data_dict = {
    'students': ["Amy", "Bernadette", "Penny"],
    'scores': [99, 80, 59],
}

grades_data = pd.DataFrame(data_dict)
print(grades_data)
grades_data.to_csv("new_grades.csv", index=False)