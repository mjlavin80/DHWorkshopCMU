# a one-line comment
""" a multiline comment
all lines between triple-quotes
will be treated as a block of code.
You can also this format for complex strings
"""
#strings

#a is a variable set to equal the string "Hello World!"
a = "Hello World!"
#printing in Python 3 requires parentheses!
print(a)

#b is also a string
b = """hello world!"""
# by assigning the triple-quoted area to a variable
print(type(b))

#Python also has integers and float-point numbers.
#an integer
c = 5

#a float
d = 5.0

#returns True
a == b

#returns False
type(a) == type(b)

#ways to group types together
#This is a list with three items. Each item is a string. Lists are useful for structuring data and going through each item one at a time.
myList = ["hi", "my", "friend"]
print(myList[0])

#This is a tuple with three items. Each item is a string. Tuples are like lists but immutable.
myTuple = ("hi", "my", "friend")
print(myTuple[0])

#This is a dictionary. Unlike lists, dictionaries have keys and values.
myDict = {"first":"hi", "second": "my", "third":"friend"}
print(myDict["first"])
