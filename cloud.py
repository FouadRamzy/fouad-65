import re
from collections import Counter
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

with open('paragraphs.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

# إزالة الرموز غير الأبجدية وتقسيم النص إلى كلمات
words = re.findall(r'\b\w+\b', text)

# إزالة الكلمات التوقف
words = [word for word in words if word not in stop_words]

# عد كمية كل كلمة
word_freq = Counter(words)

# عرض ترتيب تكرار الكلمات على الشاشة
for word, freq in word_freq.items():
    print(f'{word}: {freq}')
