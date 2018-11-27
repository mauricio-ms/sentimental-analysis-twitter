import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from array_utils import *


def plot(config, title):
    labels = map(get_key, config)
    values = map(get_value, config)
    x = np.arange(len(values))
    plt.title(title)
    plt.bar(x, values)
    plt.xticks(x, labels)
    plt.show()


def word_clue(text):
    plt.imshow(WordCloud().generate(text), interpolation="bilinear")
    plt.axis("off")
    plt.show()
