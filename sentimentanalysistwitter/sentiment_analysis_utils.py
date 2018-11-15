#coding=utf-8
import re
import pprint
import numpy as np
from file_utils import *

pattern_split = re.compile(r"[\s@&.,?$+]")
word_mapping = read_word_mapping()


def sentiment(text):
    sentiments = []
    words = combinations(text.lower())
    for word in words:
        if word in word_mapping:
            sentiments.append(int(word_mapping[word]))

    score = np.sum(sentiments)

    print "Sentiment for text: {}".format(score)
    print text
    pprint.pprint(sentiments)

    return {
        "score": score,
        "sentiments": sentiments
    }


def combinations(text):

    def combinations_inner(text):
        words = pattern_split.split(text)
        list_of_list_of_words = [[[text]]] + [[words[:i], words[i:]] for i in range(1, len(words))]
        list_of_words = [word for list_of_words in list_of_list_of_words for word in list_of_words]
        return set(words + [" ".join(words) for words in list_of_words])

    words = combinations_inner(text)
    list_of_words = [combinations_inner(word) for word in words]
    return set([word for words in list_of_words for word in words])



