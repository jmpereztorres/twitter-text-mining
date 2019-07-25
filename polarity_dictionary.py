# Load Polarity Dictionary

def load_dic(filename):
    d = {}
    for line in open(filename):
        clean = line.strip()
        if len(clean) > 0 and clean[0] != '#':
            palabra, pol = clean.split()
            d[palabra] = pol
    return d

polarity_dic = load_dic("../corpus/ElhPolar_esV1.lex")
type(polarity_dic)

def add_word (word, sentiment, thedict=polarity_dic):
    thedict[word] = sentiment

p = "positive"
n = "negative"
add_word(":)", p)
add_word(":-)", p)
add_word(":(", n)
add_word(";-)", p)
add_word('=)', p)
add_word(":/", n)
add_word(";)", p)
