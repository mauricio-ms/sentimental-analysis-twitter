# coding=utf-8
import matplotlib.pyplot as plt
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


def scatter(classes, weights):
    plt.clf()
    cords = np.random.random_integers(0, max(weights), len(classes))
    for i, c in enumerate(classes):
        x = cords[i]
        y = x + i
        plt.scatter(x, y, s=weights[i], alpha=0.5)
        plt.text(x + 0.3, y + 0.3, c, fontsize=9)
    return plt
