"""
One thing that makes Python so powerful is libraries.
Libraries allow users to build and share blocks of code that do all kinds of things that would forever to rebuild from scratch.
One of my favorite shortcuts is Counter, which comes from the collections library
"""

myList = ["the", "at", "he", "she", "the", "it", "me", "the", "you", "he"]

from collections import Counter
myCounter = Counter(myList)

#counters combine the flexibility and performance of dictionaries with the sortability of lists!
print(myCounter)

#some other fantastic libraries include matplotlib, numpy, pandas, sklearn, gensim, nltk, and sqlite3
#more on those later!
