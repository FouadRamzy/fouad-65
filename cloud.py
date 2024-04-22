import nltk
from collections import Counter
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))

with open('paragraphs.txt', 'r', encoding='utf-8') as file:
    
    text = file.read().lower()
    
words = nltk.findall(r'\b\w+\b', text)

words = [word for word in words if word not in stop_words]

word_freq = Counter(words)

for word, freq in word_freq.items():
    print(f'{word}: {freq}')
