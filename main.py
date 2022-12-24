import pandas as pd

#This is the hard way of doing this
# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

#Instead we can use the csv library:
# import csv

# with open("weather_data.csv") as weather:
#      data = csv.reader(weather) #creates csv reader object (I can iterate through this)
#      #To extract temperature for every row and save it to list of integers:
#      temperatures = []
#      for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#      print(temperatures) 

#Pandas Library: Python data analysis library
data = pd.read_csv("weather_data.csv")
#print(type(data["temp"])) --> pd series
#print(data) #prints the pd dataframe

# data_dict = data.to_dict() converts dataframe into dictionary
# print(data_dict)

#temp_list = data["temp"].to_list()#converts panda series into list
# LONG WAY: avg = sum(temp_list)/len(temp_list) #average temp
#print(temp_list)
#print(avg)


#PANDAS WAY:
#print(data["temp"].mean())
#print(data["temp"].max())
#print(data["condition"]) #prints the "Condition" column
#print(data[data.day == "Monday"])
#print(data[data["day"] == "Monday"]) these last two are the same thing

#high = data["temp"].max()
#print(data[data["temp"] == high])
#monday = data[data.day == "Monday"]

#monday_temp = monday.temp
#print(monday_temp)
#monday_farenheit = int(monday_temp) * 9/5 + 32

#print(monday_farenheit)

#CREATE DATAFRAME FROM SCRATCH
data_dict = {"students": ["tim", "Morgan", "Taylor"], "grades":[76, 80, 65]}
df = pd.DataFrame(data_dict)
print(df)
data.to_csv("new_file.csv")

