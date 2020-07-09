"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# imports for the method 3 file open
import os
import sys 

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
print("with open")
print()
with open("./intro-python-1/foo.txt") as f:
    print(f.read())
    
print()    
print("file open")
file = open("./intro-python-1/foo.txt", "r")
print(file.read())
file.close()

print()
print("__location__ method ")
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'foo.txt'));
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
print()
print("__location__ method create bar text and fill")

barfile = open(os.path.join(__location__, 'bar.txt'), 'w+');

for i in range(5):
     barfile.write(f"This is line {i + 1} \r\n ") 

barfile.close() 

f = open(os.path.join(__location__, 'bar.txt'));
print(f.read())
f.close()
