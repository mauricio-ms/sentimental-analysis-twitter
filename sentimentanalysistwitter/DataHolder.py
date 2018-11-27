from sentiment_analysis_utils import *


class DataHolder:

    def __init__(self, tweets, candidates):
        print "Calculating ..."
        self.candidates = candidates
        sentiment_tuples = map(lambda t: [sentiment(t[1]), join(reduce_by_key(adder, map(lambda x: (x, 1), pattern_split.split(t[1]))), candidates)], tweets)
        sentiment_tuples = map(lambda x: [x[0], [max(x[1], key=get_value)[0]]],
                               filter(lambda x: is_not_empty(x[1]), sentiment_tuples))
        sentiment_tuples = flat_map_values(sentiment_tuples)
        sentiment_tuples = map(lambda s: [s[1], s[0]], sentiment_tuples)

        score_tuples = reduce_by_key(adder, map(lambda x: (x[0], x[1].get("score")), sentiment_tuples))
        words_tuples = flat_map_double_array(map(lambda x: (x[1].get("words"), x[1].get("sentiments")), sentiment_tuples))
        words_tuples = sorted(words_tuples, key=get_key)
        self.worse_words_tuples = reduce_by_key(concat, map(lambda x: (get_key(x), 1), filter(lambda y: get_value(y) < 0, words_tuples)))
        self.better_words_tuples = reduce_by_key(concat, map(lambda x: (get_key(x), 1), filter(lambda y: get_value(y) >= 0, words_tuples)))
        self.sentiment_tuples = reduce_by_key(concat, map(lambda x: (x[0], x[1].get("sentiments")), sentiment_tuples))

        group_by_candidates = [(key, sum(1 for item in group)) for key, group in
                                    groupby(sorted(sentiment_tuples, key=get_key), get_key)]
        self.counts = join(group_by_candidates, candidates)
        self.scores = join(score_tuples, candidates)