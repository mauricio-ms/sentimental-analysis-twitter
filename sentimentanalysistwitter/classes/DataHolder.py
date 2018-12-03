from sentimentanalysistwitter.scripts.sentiment_analysis_utils import *


class DataHolder:

    def __init__(self, candidates, sentiment_tuples):
        print "Calculating ..."
        self.candidates = candidates
        score_tuples = reduce_by_key(adder, map(lambda x: (x[0], x[1].get("score")), sentiment_tuples))
        words_tuples = map(lambda x: (x[0], x[1].get("words"), x[1].get("sentiments")), sentiment_tuples)
        words_tuples = [list(group) for key, group in groupby(words_tuples, key=get_key)]
        words_tuples = [(item[0], flat_map_double_array([item[1:]])) for word_tuple in words_tuples for item in word_tuple]
        words_tuples = reduce_by_key(concat, words_tuples)
        self.worse_words_tuples = map(lambda x: (get_key(x), reduce_by_key(concat,
                                                                           filter(lambda y: get_value(y) < 0, get_value(x)))), words_tuples)
        self.better_words_tuples = map(lambda x: (get_key(x), reduce_by_key(concat,
                                                                            filter(lambda y: get_value(y) >= 0, get_value(x)))), words_tuples)
        self.sentiment_tuples = reduce_by_key(concat, map(lambda x: (x[0], x[1].get("sentiments")), sentiment_tuples))

        group_by_candidates = [(key, sum(1 for _ in group)) for key, group in
                               groupby(sorted(sentiment_tuples, key=get_key), get_key)]
        self.counts = join(group_by_candidates, candidates)
        self.scores = join(score_tuples, candidates)