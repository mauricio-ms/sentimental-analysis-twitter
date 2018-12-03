# coding=utf-8
from sentimentanalysistwitter.scripts.chart_utils import *


class PlotGenerator:

    def __init__(self, folder, data_holder):
        self.folder = "../../resources/plots/{}".format(folder)
        self.data_holder = data_holder

    def plot(self):
        plot(self.data_holder.counts, u"Quantidade de Tweets por Candidato")\
            .savefig(self.build_uri_to_save("quantidade-de-tweets-por-candidato"))
        plot(self.data_holder.scores, u"Sentimento por Candidato")\
            .savefig(self.build_uri_to_save("sentimento-por-candidato"))

        mean_scores = map(lambda x: (get_key(x), np.mean(get_value(x))), self.data_holder.scores)
        plot(mean_scores, u"Sentimento por Candidato (Média)") \
            .savefig(self.build_uri_to_save("sentimento-por-candidato-media"))

        median_scores = map(lambda x: (get_key(x), np.median(get_value(x))), self.data_holder.scores)
        plot(median_scores, u"Sentimento por Candidato (Mediana)") \
            .savefig(self.build_uri_to_save("sentimento-por-candidato-mediana"))

        sentiments = join(self.data_holder.sentiment_tuples, self.data_holder.candidates)
        worse_values = map(lambda x: (get_key(x), filter(lambda y: y < 0, get_value(x))), sentiments)
        better_values = map(lambda x: (get_key(x), filter(lambda y: y >= 0, get_value(x))), sentiments)
        worse_mean_values = map(lambda x: (get_key(x), np.mean(get_value(x))), worse_values)
        better_mean_values = map(lambda x: (get_key(x), np.mean(get_value(x))), better_values)

        plot(worse_mean_values, u"Pior valor médio por Candidato") \
            .savefig(self.build_uri_to_save("pior-valor-medio-por-candidato"))
        plot(better_mean_values, u"Melhor valor médio por Candidato") \
            .savefig(self.build_uri_to_save("melhor-valor-medio-por-candidato"))

        worse_most_frequently_values = map(map_value_to_most_common, worse_values)
        better_most_frequently_values = map(map_value_to_most_common, better_values)
        plot(worse_most_frequently_values, u"Pior valor mais frequente por Candidato") \
            .savefig(self.build_uri_to_save("pior-valor-mais-frequente-por-candidato"))
        plot(better_most_frequently_values, u"Melhor valor mais frequente por Candidato") \
            .savefig(self.build_uri_to_save("melhor-valor-mais-frequente-por-candidato"))

        for candidate_worse_words_tuples in self.data_holder.worse_words_tuples:
            candidate = candidate_worse_words_tuples[0]
            worse_words_tuples = candidate_worse_words_tuples[1]
            worse_words_as_text = "".join(map(multiply_word, worse_words_tuples))
            word_clue(worse_words_as_text, "Piores Palavras - {}".format(candidate)) \
                .savefig(self.build_uri_to_save("word-clue-piores-palavras-{}".format(candidate)))

        for candidate_better_words_tuples in self.data_holder.better_words_tuples:
            candidate = candidate_better_words_tuples[0]
            better_words_tuples = candidate_better_words_tuples[1]
            better_words_as_text = "".join(map(multiply_word, better_words_tuples))
            word_clue(better_words_as_text, "Melhores Palavras - {}".format(candidate)) \
                .savefig(self.build_uri_to_save("word-clue-melhores-palavras-{}".format(candidate)))

    def build_uri_to_save(self, file_name):
        return "{}/{}".format(self.folder, file_name)