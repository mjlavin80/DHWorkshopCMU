#read dictionary.com values into a Python dictionary
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
unigram_tagger = nltk.UnigramTagger(t)
int_uni_pos = unigram_tagger.tag(tokens_all)

#remove function words from test texts: determiners, prepositions, conjunctions, and pronouns


#convert full term lists to lists with each term listed only once (aka a "set")
#loop through each term set, execute germ_lat function to derive "the ratio of pre- and post-twelfth-century words"
#print for each text a title, year of publication, origina word count (pre-processing), unique term count (after removing function words) and ratio
