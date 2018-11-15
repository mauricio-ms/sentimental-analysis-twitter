#coding=utf-8
from sentiment_analysis_utils import *

print "main"

# text = u"""
# RT @MBLivre: O PT quer que Haddad seja o líder da campanha para que Lula seja solto.
# Esperamos que seja ele mesmo: tomou um pau no primeir…
# """
# text = u"Graças a Deus que as eleições acabaram. Foda-se o bolsonaro, Mourão, Lula, Haddad, Ciro, PT, PSL e tudo mais."

# text = u"Ferramenta de Deteccao e Remocao de Malware"

# text = u"""
# 2
# RT @JeanMessiha: Cherchez l’intrus :
# 1) TOUS les médias sont contre le #Brexit
# 2) TOUS les médias sont contre #Trump
# 3) TOUS les médias son…
# """

text = u"RT @Drica_Patriota: Incrível, #Bolsonaro nem assumiu a presidência ainda e a economia já está dando sinal de melhoria. Grupo Kyly anuncia i…"

sentiment(text)

# def sentiment(text):
#     words = pattern_split.split(text.lower())
#     sentiments = []
#     print "\nSentiment for text: "
#     print text
#     for word in words:
#         # print word
#         if word in word_mapping:
#             sentiments.append(int(word_mapping[word]))
#             # print word_mapping[word]
#         else:
#             sentiments.append(0)
#             # print 0
#     score = 0
#     if sentiments:
#         score = float(sum(sentiments))/math.sqrt(len(sentiments))
#
#     print "Score:"
#     print score
#
#     return {
#         "score": score,
#         "sentiments": sentiments
#     }

