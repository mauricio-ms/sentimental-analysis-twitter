from functools import reduce


import matplotlib.pyplot as plt
# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
#from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# # for tweet in tweets.find():
# #     pprint.pprint(tweet)
#
# tweets = []
# for tweet in db.tweets.find({}, {"text": 1, "_id": 0}):
#     tweets.append(tweet.get("text"))
#
# text = "".join(tweets)
# print text
#
# # Start with one review:
# # text = "Oi meu amigo oi minha joana oi jose oi ana ana"
#
# # Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)
#
# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()