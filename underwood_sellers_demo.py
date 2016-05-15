import csv, nltk, glob
#read dictionary.com values into a Python dictionary
dictionary_com = {}
with open('Etymologies.txt') as myfile:
    for line in csv.reader(myfile, dialect="excel-tab"):
        dictionary_com[line[0]] = int(line[1])

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

#this is a huge tagset, so training the tagger will take a long time!
unigram_tagger = nltk.UnigramTagger(t)

#print(dictionary_com)
#loop, read() files
text = glob.glob('./full_text/*.txt')
all_texts_pos = []
for i in text:
    #open and read()
    with open(i) as f:
        md_text = f.read()
    #tokenize, lowercase, remove newlines and tabs, strip punctuation and numbers
    #convert newlines and tabs to spaces
    md_text = md_text.replace('\n', ' ').replace('\t', ' ')
    #remove no-alpha characters, convert all to lowercase
    md_no_punct = ''.join(char.lower() if char.isalpha() else ' ' for char in md_text )
    #tokenize and drop empty list items
    md_tokens = [i for i in md_no_punct.split(' ') if i != '']
    #pos tag with unigram tagger
    uni_pos = unigram_tagger.tag(md_tokens)
    #append to all_texts
    all_texts_pos.append(uni_pos)


function_symbols = ['DT', 'IN', 'CC', 'PRP,' 'PRP$', 'WP', 'WP$']
token_sets = []
for token_list in all_texts_pos:
    #remove function words from test texts: determiners, prepositions, conjunctions, and pronouns
    token_set = []
    for token in token_list:
        if token[1] not in function_symbols:
            token_set.append(token[0])
    #convert full term lists to lists with each term listed only once (aka a "set")
    token_set = set(token_set)
    token_sets.append(token_set)

#loop through each term set, derive "the ratio of pre- and post-twelfth-century words"
ratios =[]
for token_set in token_sets:
    pre = 0
    post = 0
    for token in token_set:
        try:
            year = dictionary_com[token]
            if year < 1100:
                pre += 1
            if year > 1100:
                post +=1
        except:
            pass
    ratio = 1.0*(pre/post)
    ratios.append(ratio)
#print for each text
titles = [i.replace('./full_text/', '').replace('.txt', '') for i in text]
orig_lengths = [len(i) for i in all_texts_pos]
length_of_sets = [len(i) for i in token_sets]
set_to_len_ratio = [1.0*(i[0]/i[1]) for i in zip(length_of_sets, orig_lengths)]
for i in zip(titles, orig_lengths, length_of_sets, set_to_len_ratio, ratios):
    print(i)
