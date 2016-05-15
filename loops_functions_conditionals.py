#loops, functions, conditionals
#loops are the best in Python. They let you go through all the items in a list, or anything else that's "iterable"
myList = ["the", "at", "he", "she", "it", "me", "you"]

#note that Python uses indented newlines to tell the computer we're still "in" the the loop
for i in myList:
     print(i)

#functions are a way to store code so we can do the sam ething over and over without retyping a bunch of things.
def myFunction(word):
    print(word, " is a word in myList")

#you always create a function then call it. Like this loop that calls myFunction for each item.
for i in myList:
     myFunction(i)

#conditionals allow you to do something if some condition is True (or False)
#we use elif to stack conditionals, and else to set the result if none of ourifs are True
a = "the"
if a == "me":
    print("yes!")
elif a == "you":
    print("never!")
else:
    print("aha!")

#we can also mix conditionals with loops and functions
for i in myList:
     if i == "the::
         myFunction(i)
     elif i == "you":
         myFunction(i)
     else:
         myFunction(i) 
