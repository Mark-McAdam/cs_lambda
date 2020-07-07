# stupid addition takes two values(x, y)
#     if x is str and y is str 
#         change both value to int and sum 
#     if x is int and y is int
#         change both value to string and concatenate
#     else return none     


def stupid_addition(x,y):
    if isinstance(x, str) and isinstance(y, str):
        return (int(x) + int(y))
    elif isinstance(x, int) and isinstance(y, int):
        return (str(x) + str(y))
    else: 
        return ("none")

print("1 and 2 string", stupid_addition("1", "2"))
print("1 and 2 int", stupid_addition(1, 2))
print("1 and 2 different", stupid_addition("1", 2))