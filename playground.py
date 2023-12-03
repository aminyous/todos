import csv

with open("file/temperatures.csv", "r") as file:
    data = list(csv.reader(file))

print(data)

