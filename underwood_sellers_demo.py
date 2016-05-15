import csv
#read dictionary.com values into a Python dictionary
dictionary_com = {}
with open('Etymologies.txt') as myfile:
    for line in csv.reader(myfile, dialect="excel-tab"):
        dictionary_com[line[0]] = line[1]

print(dictionary_com)

#loop, read() files
#tokenize, lowercase, remove newlines and tabs, strip punctuation and numbers
#part of speech tagging with nltk unigram tagger
from nltk.corpus import masc_tagged

tags = []
for i in masc_tagged.fileids():
    if len(tags) > 150000:
        break
    if 'written' in i:
        tags.extend(masc_tagged.tagged_words(i))

t = []
t.append(tags)

# if running this script in binder, comment out lines 5 through 15 and remove the triple quotes on lines 18 and 21 top uncomment the pickle version.
"""
import pickle
t = pickle.load(open('tagger.p', 'rb'))
"""

unigram_tagger = nltk.UnigramTagger(t)
int_uni_pos = unigram_tagger.tag(tokens_all)

#remove function words from test texts: determiners, prepositions, conjunctions, and pronouns


#convert full term lists to lists with each term listed only once (aka a "set")
#loop through each term set, execute germ_lat function to derive "the ratio of pre- and post-twelfth-century words"
#print for each text a title, year of publication, origina word count (pre-processing), unique term count (after removing function words) and ratio
