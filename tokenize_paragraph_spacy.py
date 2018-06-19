import spacy

# check out the librery on https://spacy.io

# spaCy excels at large-scale information extraction tasks.
# It's written from the ground up in carefully memory-managed Cython.
# Independent research has confirmed that spaCy is the fastest in the world.
# If your application needs to process entire web dumps, spaCy is the library you want to be using.

nlp = spacy.load('en')

s = 'Mr. John Johnson Jr. was born in the U.S.A but earned his Ph.D. in Israel before joining Nike Inc. \
    as an engineer. He also worked at craigslist.org as a business analyst.'

tokens = nlp(s)

for sent in tokens.sents:
    print(sent.string.strip())