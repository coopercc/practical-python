# pcost.py
#
# Exercise 1.27

total_cost = 0

with open("Data/portfolio.csv", "rt") as f:
    headers = next(f)
    for line in f:
        data = line.split(",")
        total_cost = total_cost + (int(data[1]) * float(data[2]))

print("Total Cost", total_cost)
