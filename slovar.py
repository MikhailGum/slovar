import pandas as pd
from collections import Counter
from pymystem3 import Mystem

def data_freq(string: str):
    data_frame_dict = {
        'word': [],
        'frequency': []
    }
    for k, v in Counter(string.lower().split()).items():
        data_frame_dict['word'].append(k)
        data_frame_dict['frequency'].append(v)

    return pd.DataFrame(data_frame_dict)


f = open('onegin.txt', 'r')
text = f.read()
m = Mystem()
lemmas = m.lemmatize(text)
text_lemmas = ' '.join(lemmas)
list_words = data_freq(text_lemmas)
print(list_words.sort_values('frequency', ascending=False))
list_words.to_csv("list_words.csv")
# Нужно дабавить чистку от знаков препинания и не символов