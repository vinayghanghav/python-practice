from collections import Counter

def word_frequency(sentence):
    words = sentence.split()
    return Counter(words)

print(word_frequency("data science is fun data is powerful"))
