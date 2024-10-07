import requests
import os
import itertools
from nltk.stem import PorterStemmer

def load_word_list():
    # Load word list from a publicly available dictionary source
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    response = requests.get(url)
    if response.status_code == 200:
        return set(response.text.splitlines())
    else:
        raise Exception("Unable to load word list from the internet.")

def generate_permutations(word, english_words):
    word = word.lower()
    suffixes = ["s", "ed", "ing", "er", "est", "ly", "ness", "ment", "tion", "y", "able", "ful", "ize", "ous", "ship", "less"]
    prefixes = ["re", "un", "dis", "in", "im", "pre", "mis", "non", "over", "under", "out", "sub", "trans"]
    
    generated_words = set()
    
    # Adding suffixes
    for suffix in suffixes:
        generated_words.add(word + suffix)

    # Adding prefixes
    for prefix in prefixes:
        generated_words.add(prefix + word)

    # Adding both prefix and suffix
    for prefix in prefixes:
        for suffix in suffixes:
            generated_words.add(prefix + word + suffix)

    # Adding internal letter combinations
    for i in range(1, len(word)):
        generated_words.add(word[:i] + word[i:].capitalize())
    
    # Adding permutations with prefixes and suffixes combined in various orders
    for num_prefixes in range(1, 3):
        for prefix_comb in itertools.combinations(prefixes, num_prefixes):
            for suffix in suffixes:
                generated_words.add(''.join(prefix_comb) + word + suffix)
    
    # Include the input word if it's in the dictionary
    if word in english_words:
        generated_words.add(word)
    
    # Adding stemmed version of the word and related forms
    stemmer = PorterStemmer()
    stemmed_word = stemmer.stem(word)
    for suffix in suffixes:
        generated_words.add(stemmed_word + suffix)
    if stemmed_word in english_words:
        generated_words.add(stemmed_word)
    
    # Check against dictionary
    valid_words = [w for w in generated_words if w in english_words]
    
    return valid_words

def get_permutations(word):
    english_words = load_word_list()
    return generate_permutations(word, english_words)

if __name__ == "__main__":
    try:
        english_words = load_word_list()
        input_word = input("Enter a word: ")
        permutations = generate_permutations(input_word, english_words)
        print("Permutations:", permutations)
    except Exception as e:
        print(e)