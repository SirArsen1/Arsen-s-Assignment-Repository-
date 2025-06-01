# #with open("example week 7.txt", "a") as append_file:
#     #append_file.write("\nMore content!")
# try:
#     with open("example week 7.txt") as test_file:
#         for l in test_file:
#             line = l.replace("\n", "")
#             print(f'''-----------------------------------
#     {line}''')
#         print(test_file.read())
# except FileNotFoundError:
#     print("File not found")

# with open("new_example_file.txt", "w") as f:
#     f.write("Hello world!")
# with open("new_example_file.txt", "r") as f:
#     print(f.read())

# user_name = input("Enter your name, please: ")
# week_input = None
# while week_input is None:
#     try:
#         week_input = int(input("please, write one number this time: "))
#     except ValueError:
#         print("Please enter a number.")
#
# print(f"Hi {user_name}, we hope you enjoy learning Python here!\nYour github repo should look like this:")
# print("assignments/")
# for i in range(int(week_input)):
#     print(f"    week{i+1}/")

# with open("Fruits.csv") as fruits:
#     for line in fruits:
#         line = line.replace("\n", "")
#         print(line)


# fruit_prices = {}
# with open("Fruits.csv") as file:
#     next(file)
#     for line in file:
#         parts = line.strip().split(",")
#         if len(parts) >= 2:  # Make sure we have at least two columns
#             name = parts[0]
#             price = float(parts[1])
#             fruit_prices[name] = price
#
# print(fruit_prices)

import csv
# rows = []
#
# with open('fruits.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)
#         rows.append(row)
#
# for row in rows:
#     name = row["Fruit"]
#     price = row["Price per kg"]
#     origin = row["Origin"]
#     print(f"{name:11s}", end=" ")
#     print(f"{float(price):5.2f} ", end=" ")
#     print(f"{origin}")
#     print("-------------------------------")
import random

# rows = []
#
# with open("fruits.csv") as table:
#     reader = csv.DictReader(table)
#     for row in reader:
#         row["Available"] = random.choice([True, False])
#         #print(row)
#         rows.append(row)
#
#
# for row in rows:
#     name = row["Fruit"]
#     price = row["Price per kg"]
#     origin = row["Origin"]
#     available = row["Available"]
#     print(f"{name:11s}", end = " ")
#     print(f"{float(price):5.2f}", end = " ")
#     print(f"{origin:15s}", end = " ")
#     print(f"{available}")

rows = []
fieldnames = []

def read_and_write():

    with open("fruits.csv") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            rows.append(row)

    print(fieldnames)
    print(rows)

    fieldnames.append("Availability")
    for row in rows:
        randomValue = bool(random.randint(0, 1))
        row["Availability"] = randomValue

    print(fieldnames)
    print(rows)

    with open('fruits_new.csv', 'w', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # specify fieldnames as a parameter
        writer.writeheader()  # First writeheader() then writerow()
        writer.writerows(rows)


read_and_write()
