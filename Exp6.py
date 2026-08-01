Code
import random
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


lemmatizer = WordNetLemmatizer()

text = "The boys are running and the girls are writing letters."

words = word_tokenize(text)

pos_tags = nltk.pos_tag(words)


def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

print("Morphological Analysis")
print("-----------------------")

lemmatized_words = []

for word, tag in pos_tags:
    if word.isalpha():
        lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        lemmatized_words.append(lemma)
        print(f"{word:12} -> {lemma}")


bigram = {}

for i in range(len(lemmatized_words) - 1):
    current = lemmatized_words[i]
    next_word = lemmatized_words[i + 1]

    if current not in bigram:
        bigram[current] = []

    bigram[current].append(next_word)


current = random.choice(lemmatized_words)
generated = [current]

for i in range(9):
    if current in bigram:
        current = random.choice(bigram[current])
        generated.append(current)
    else:
        break

print("\nGenerated Text")
print("--------------")
print(" ".join(generated))
