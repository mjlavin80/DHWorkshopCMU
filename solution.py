#import the nltk library and glob
import nltk, glob, csv
#import a list of stopwords in English
from nltk.corpus import stopwords
s = stopwords.words('english')

#comment lines 4 and 5 and uncomment the block below if running with mybinder
"""
s = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
"""

#use "with open" and "read" to store a new text as a variable
with open('./full_text/king_in_yellow.txt') as t:
    #could be any other file
    md_text = t.read()

#use code from my snippets to remove newlines, tabs, punctuation etc and lowercase all text
#convert newlines and tabs to spaces
md_text = md_text.replace('\n', ' ').replace('\t', ' ')
#remove no-alpha characters, convert all to lowercase

md_no_punct = ''.join(char.lower() if char.isalpha() else ' ' for char in md_text )

#convert your text to a list of terms using tokenization
#tokenization: convert string of moby_dick to a list of terms
md_tokens = [i for i in md_no_punct.split(' ') if i != '']

#create empty lists called matchedStopwords and myTextMinusStops
matchedStopwords = []
myTextMinusStops = []
#loop through your list of terms.
for i in md_tokens:
    #check to see if the term is in the stopwords list
    if i in s:
        #if yes, add to list called matchedStopwords
        matchedStopwords.append(i)
    else:
        #if not, add to list called myTextMinusStops
        myTextMinusStops.append(i)
#check myTextMinusStops to make sure no stop words are in it
print(myTextMinusStops)
#convert your matched list to a Counter and print it
from collections import Counter
myCounter = Counter(matchedStopwords)
print(myCounter)
