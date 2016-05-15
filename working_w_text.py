#reading text from files (note that this is a relative path, so the text file must be in your current working directory)
with open("full_text/moby_dick.txt") as md:
    md_text = md.read()

print(type(md_text))

#convert newlines and tabs to spaces
md_text = md_text.replace('\n', ' ').replace('\t', ' ')
#remove no-alpha characters, convert all to lowercase

md_chars = []
for char in md_text:
    char = char.lower()
    if char.isalpha():
        md_chars.append(char)
    else:
        md_chars.append(' ')
md_no_punct = ''.join(md_chars)

#or with list comprehension, a loop shortcut ... much faster!
#md_no_punct = ''.join(char.lower() if char.isalpha() else ' ' for char in md_text )

#tokenization: convert string of moby_dick to a list of terms
md_tokens = [i for i in md_no_punct.split(' ') if i != '']

#slicing a list. There are better ways to remove front and back matter, but I wanted to show you how to traverse a list
md_minus_front_back = md_tokens[3892:-2994]

#matching ... get all words that end with 'ing'
ing_words = []
for i in md_minus_front_back:
    if i[-3:] == 'ing':
        ing_words.append(i)

from collections import Counter
ing_counts = Counter(ing_words)
