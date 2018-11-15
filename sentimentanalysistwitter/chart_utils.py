import matplotlib.pyplot as plt
import numpy as np


def plot(values, labels, title):
    x = np.arange(len(values))
    plt.title(title)
    plt.bar(x, values)
    plt.xticks(x, labels)
    plt.show()
