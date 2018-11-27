import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from array_utils import *


def plot(config, title):
    plt.clf()
    labels = map(get_key, config)
    values = map(get_value, config)
    x = np.arange(len(values))
    plt.title(title)
    plt.bar(x, values)
    plt.xticks(x, labels)
    return plt


def word_clue(text, title):
    plt.clf()
    plt.title(title)
    plt.imshow(WordCloud().generate(text), interpolation="bilinear")
    plt.axis("off")
    return plt
