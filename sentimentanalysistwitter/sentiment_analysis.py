# coding=utf-8
from pymongo import MongoClient

from chart_utils import *
from sentiment_analysis_utils import *

print "Connecting to Mongo Database ..."

client = MongoClient("127.0.0.1", 27017)
db = client.tweetsDb

pattern_split = re.compile(r"[\s@&.?$+]+")
word_mapping = read_word_mapping()


def mapper_tweets(tweet):
    return [tweet.get("id"), tweet.get("full_text"),
            map(lambda u: u.get("name"), tweet.get("entities").get("user_mentions"))]


print "Reading Tweets ..."
projection_tweets = {"id": 1, "full_text": 1, "entities": 1, "_id": 0}
tweets = map(mapper_tweets, list(db.oldCandidateTweets.find({}, projection_tweets)))

print "Calculating ..."
candidates = read_candidate_mapping()
candidates = map(lambda x: (x.strip().split(",")[0], x.strip().split(",")), candidates)
candidates = flat_map_values(candidates)
candidates = set(map(lambda c: (c[1], c[0]), candidates))

sentiment_tuples = map(lambda t: [sentiment(t[1]), join(reduce_by_key(adder, map(lambda x: (x, 1), pattern_split.split(t[1]))), candidates)], tweets)
sentiment_tuples = map(lambda x: [x[0], [max(x[1], key=get_value)[0]]],
                       filter(lambda x: is_not_empty(x[1]), sentiment_tuples))
sentiment_tuples = flat_map_values(sentiment_tuples)
sentiment_tuples = map(lambda s: [s[1], s[0]], sentiment_tuples)

#reduce_by_key(adder, map(lambda x: max(x, key=get_value), filter(is_not_empty, map(lambda tweet: join(reduce_by_key(adder, map(lambda x: (x, 1), pattern_split.split(tweet[1]))), candidates), tweets))))

group_by_candidates = [(key, sum(1 for item in group)) for key, group in
                       groupby(sorted(sentiment_tuples, key=get_key), get_key)]
score_tuples = reduce_by_key(adder, map(lambda x: (x[0], x[1].get("score")), sentiment_tuples))
words_tuples = flat_map_double_array(map(lambda x: (x[1].get("words"), x[1].get("sentiments")), sentiment_tuples))
words_tuples = sorted(words_tuples, key=get_key)
worse_words_tuples = reduce_by_key(concat, map(lambda x: (get_key(x), 1), filter(lambda y: get_value(y) < 0, words_tuples)))
better_words_tuples = reduce_by_key(concat, map(lambda x: (get_key(x), 1), filter(lambda y: get_value(y) >= 0, words_tuples)))

sentiment_tuples = reduce_by_key(concat, map(lambda x: (x[0], x[1].get("sentiments")), sentiment_tuples))

# "".split(tweets[0], 1)
# join(map(lambda x: (x, x), pattern_split.split(tweets[0][1])), candidates)
# usar combinations ver historico git
# pattern_split = re.compile(r"[\s@&.,?$+]")
# newWay = join([(item, 1) for list in map(lambda x: (pattern_split.split(x[1])), tweets) for item in list], candidates)
# max(reduce_by_key(adder, map(lambda x: (x, 1), pattern_split.split(tweets[147][1]))), key=get_value)
# newWay = reduce_by_key(adder, map(lambda x: max(x, key=get_value), filter(is_not_empty, map(lambda tweet: join(reduce_by_key(adder, map(lambda x: (x, 1), pattern_split.split(tweet[1]))), candidates), tweets))))
print "Results:"
counts = join(group_by_candidates, candidates)
plot(counts, u"Quantidade de Tweets por Candidato")

scores = join(score_tuples, candidates)
plot(scores, u"Sentimento por Candidato")
mean_scores = map(lambda x: (get_key(x), np.mean(get_value(x))), scores)
plot(mean_scores, u"Sentimento por Candidato (Média)")
median_scores = map(lambda x: (get_key(x), np.median(get_value(x))), scores)
plot(mean_scores, u"Sentimento por Candidato (Mediana)")

sentiments = join(sentiment_tuples, candidates)
worse_values = map(lambda x: (get_key(x), filter(lambda y: y < 0, get_value(x))), sentiments)
better_values = map(lambda x: (get_key(x), filter(lambda y: y >= 0, get_value(x))), sentiments)
worse_mean_values = map(lambda x: (get_key(x), np.mean(get_value(x))), worse_values)
better_mean_values = map(lambda x: (get_key(x), np.mean(get_value(x))), better_values)

plot(worse_mean_values, u"Pior valor médio por Candidato")
plot(better_mean_values, u"Melhor valor médio por Candidato")

worse_most_frequently_values = map(map_value_to_most_common, worse_values)
better_most_frequently_values = map(map_value_to_most_common, better_values)
plot(worse_most_frequently_values, u"Pior valor mais frequente por Candidato")
plot(better_most_frequently_values, u"Melhor valor mais frequente por Candidato")

worse_words_as_text = "".join(map(multiply_word, worse_words_tuples))
better_words_as_text = "".join(map(multiply_word, better_words_tuples))
word_clue(worse_words_as_text)
word_clue(better_words_as_text)
