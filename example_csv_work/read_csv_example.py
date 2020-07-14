# import os to work with filepath, and csv to work with csv file
import os

# do not name the file csv or it will try importing itself
import csv

print("initial example: ")
print("*" * 25)
file = open("sample.csv")
csv_reader = csv.reader(file)
for row in csv_reader:
    print(row)


print()
print("__location__ example: ")
print("*" * 25)

# set location of file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# open file
file = open(os.path.join(__location__, "sample.csv"))
csv_reader = csv.reader(file)
next(csv_reader)
for row in csv_reader:
    print(row)


print()
print("with open example: ")
print("*" * 25)


with open("sample.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        # join is built in function and takes items from a list
        # and concatenates on whatever is in the parentheses
        print(", ".join(row))
