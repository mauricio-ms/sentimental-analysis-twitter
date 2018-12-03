import numpy as np
import matplotlib.pyplot as plt
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
#
# plt.scatter([2, 4, 6], [2, 4, 6], s=[8, 800, 80], c=["a", "b", "c"], alpha=0.5)
# plt.show()

import matplotlib.pyplot as plt
from numpy.random import rand


fig, ax = plt.subplots()
words = ['fascista', 'fascista']
words_positions = [1, 2]
quantities = [4, 8]
i = 0
for candidate in [('Bolsonaro', 'green'), ('Haddad', 'red')]:
    x = words_positions[i]
    y = quantities[i]
    ax.scatter(x, y,
               c=candidate[1], label=candidate[0],
               alpha=0.8, edgecolors='none')
    ax.text(x, y, words[i], fontsize=9)
    i = i + 1

ax.legend()
ax.grid(True)

plt.show()