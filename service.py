#%%
import nltk , re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from googletrans import Translator
import pandas as pd

import os , sys
current_dir = os.path.dirname(os.path.abspath(__file__))

nltk.download('punkt')
nltk.download('stopwords')

translator = Translator()

with open(f'{current_dir}/articles.txt','r',encoding='utf-8') as f : 
    content = f.readlines()

content = ''.join(content)

content = content.lower()
text_no_punctuation = re.sub(r'[^\w\s]', '', content)

words = word_tokenize(text_no_punctuation)

# 获取停用词列表
stop_words = set(stopwords.words('english'))

# 过滤停用词
filtered_words = [word for word in words if word not in stop_words]

def translate(word):
    return translator.translate(word, src='en', dest='zh-cn').text

language = []
for word in filtered_words :
    language.append({
        'dest' : word,
        'cn' : translate(word)
    })

for _ in language :
    print(_)