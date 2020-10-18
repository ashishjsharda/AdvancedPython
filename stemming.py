from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer("english")
print(stemmer.stem("reaching"))
print(stemmer.stem("blessed"))
