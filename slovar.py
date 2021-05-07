import pandas as pd
from collections import Counter
from pymystem3 import Mystem
import re


def data_freq(string: str):
    data_frame_dict = {
        'word': [],
        'frequency': []
    }
    for k, v in Counter(string.lower().split()).items():
        data_frame_dict['word'].append(k)
        data_frame_dict['frequency'].append(v)

    return pd.DataFrame(data_frame_dict)

pattern = '[a-zA-Zа-яА-ЯёЁ]+'
f = open('Семантика.txt', 'r')
text = f.read()
text_clean = ' '.join(re.findall(pattern, text))
m = Mystem()
lemmas = m.lemmatize(text_clean)
text_lemmas = ' '.join(lemmas)
list_words = data_freq(text_lemmas)
print(list_words.sort_values('frequency', ascending=False))
list_words.to_csv("list_words.csv")
# Нужно дабавить чистку от знаков препинания и не символов