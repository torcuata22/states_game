import pandas as pd

data=pd.read_csv("2018_Central_Park_Squirrel_Census.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
gray_count = len(gray) #I can do this becuase this is a series, which acts like a list
print(f"gray squirrels: {gray_count}")
cinnamon = data[data["Primary Fur Color"]  == "Cinnamon"]
cinnamon_count = len(cinnamon)
print(f"red squirrels: {cinnamon_count}")
black = data[data["Primary Fur Color"] == "Black"]
black_count = len(black)
print(f"black squirrels: {black_count}")

#to construct data frame:
squirrel_dict = {
     "Fur color":["Gray", "Cinnamon", "Black"],
     "Population":[gray_count, cinnamon_count, black_count]
     }
print (squirrel_dict)

#we need to create a pandas dataframe first:
df = pd.DataFrame(squirrel_dict)
#Now, convert dataframe into csv file:
df.to_csv("squirrel_colors.csv")
