import re

# The method has been taken from this post.
# https://stackoverflow.com/questions/4576077/python-split-text-on-sentences

# This function can split the entire text of Huckleberry Finn into sentences in about 0.1 seconds
# and handles many of the more painful edge cases that make sentence parsing non-trivial 
# e.g. "Mr. John Johnson Jr. was born in the U.S.A but earned his Ph.D. in Israel before joining 
# Nike Inc. as an engineer. He also worked at craigslist.org as a business analyst."

caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"             # to skip some common designations
suffixes = "(Inc|Ltd|Jr|Sr|Co)"    
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"  # to skip abbreviations
websites = "[.](com|net|org|io|gov)"          # to skip websites

def split_into_sentences(text):
    text = " " + text + "  "                   
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")      # <stop> token signifies end of sentence
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")        # to separate the string by <stop> token
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences