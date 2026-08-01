from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "playing", "studies", "happily", "connected", "fishing"]

print("Original Word\tStemmed Word")
print("-" * 30)

for word in words:
    print(word, "\t\t", stemmer.stem(word))
