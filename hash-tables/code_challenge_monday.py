"""Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

count = 0

list = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

for j in list:
    count += min(j)
print(count)


# the solution I talked through
# Create an empty list to hold the minimum item in each array
# append smallest item in each nested list
# Go through items in list
# sum items in the list of minimum values.

min_list = []
for integer in list:
    min_list.append(min(integer))
    total = sum(min_list)
print(total)

