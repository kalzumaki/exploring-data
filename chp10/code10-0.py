import os
print("current directory: ",os.getcwd())

with open('../data/sample_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print('Original Text: ',text[:500])

import re, nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

clean_text = ' '.join([w for w in re.sub(r'[^a-z\s]', '', text.lower()).split() if w not in stop_words])

print('\nClean Text:',clean_text[:500])

from collections import Counter # importing counter


freq = Counter(clean_text.split())
print()
print(freq.most_common(10))

from wordcloud import WordCloud

import matplotlib.pyplot as plt

wc = WordCloud(width=800, height=400, background_color='white').generate(clean_text)
plt.figure(figsize=(15,7))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()