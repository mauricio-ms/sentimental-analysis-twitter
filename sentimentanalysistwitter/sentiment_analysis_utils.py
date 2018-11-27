# coding=utf-8
import pprint
import re
import math
from array_utils import *
from file_utils import *

pattern_split = re.compile(r"[\s@&.,?$+]")
word_mapping = read_word_mapping()


def sentiment(text):
    """
    sum [i=1 ... m] sentiment(Pi) / sqrt(len(text))
    len(text) -> Number of words inside text
    sentiment(Pi) -> Sentiment value for each word
    """
    sentiments = []
    words_evaluated = []
    words = pattern_split.split(text.lower())
    for word in words:
        if word in word_mapping:
            sentiments.append(int(word_mapping[word]))
            words_evaluated.append(word)

    score = float(sum(sentiments)) / math.sqrt(len(words))

    # print "Sentiment for text: {}".format(score)
    # print text
    # pprint.pprint(sentiments)

    return {
        "score": score,
        "sentiments": sentiments,
        "words": words_evaluated
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
