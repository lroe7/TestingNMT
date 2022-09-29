import os
import numpy as np
from sklearn.model_selection import train_test_split

n_sentences = 250000
# Loading English sentences
original_en_sentences = []
with open('train.en', mode='rt', encoding='utf-8') as en_file:
    for i in en_file:
        original_en_sentences.append(i.strip().split("."))
# Loading German sentences
original_es_sentences = []
with open('train.es', mode='rt', encoding='utf-8') as es_file:
    for i in es_file:
        original_es_sentences.append(i.strip().split("."))

print("English: ", original_en_sentences)
print("Spanish:", original_es_sentences)
en_sentences = [["<s>"]+sent+["</s>"] for sent in original_en_sentences]
de_sentences = [["<s>"]+sent+["</s>"] for sent in original_es_sentences]


# train_en_sentences, valid_test_en_sentences, train_de_sentences, valid_test_de_sentences = train_test_split (
#     np.array(en_sentences), np.array(de_sentences), test_size=0.2
# )
# valid_en_sentences, valid_de_sentences, test_en_sentences, test_de_sentences = train_test_split(
#     valid_test_en_sentences, valid_test_de_sentences, test_size=0.5
# )