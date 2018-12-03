# coding=utf-8
from pymongo import MongoClient
from sentimentanalysistwitter.scripts.sentiment_analysis_utils import *
from sentimentanalysistwitter.scripts.chart_utils import *
from sentimentanalysistwitter.classes.DataHolder import DataHolder
from sentimentanalysistwitter.classes.PlotGenerator import PlotGenerator
import datetime

print "Connecting to Mongo Database ..."

client = MongoClient("127.0.0.1", 27017)
db = client.tweetsDb

pattern_split = re.compile(r"[\s@&.?$+]+")
word_mapping = read_word_mapping()


def mapper_tweets(tweet):
    return [tweet.get("id"), tweet.get("full_text"),
            map(lambda u: u.get("name"), tweet.get("entities").get("user_mentions"))]


print "Starting Reading Tweets at: " + str(datetime.datetime.now())
projection_tweets = {"id": 1, "full_text": 1, "entities": 1, "_id": 0}
tweets = map(mapper_tweets, list(db.oldCandidateTweets.find({}, projection_tweets).limit(1000)))
print "Tweets read finished at: " + str(datetime.datetime.now())

# Complete wordclue
# word_clue(" ".join(map(get_value, tweets)), "teste")\
#     .savefig("../resources/plots")
# print tweets

print "Reading Candidates"
candidates = read_candidate_mapping("all_candidate_mapping.txt")
# candidates_second_round = read_candidate_mapping("second_round_candidate_mapping.txt")

print "Calculating variables from data"
sentiment_tuples = map(lambda t: [sentiment(t[1]), join(reduce_by_key(adder, map(lambda x: (x, 1), pattern_split.split(t[1]))), candidates)], tweets)
sentiment_tuples = map(lambda x: [x[0], [max(x[1], key=get_value)[0]]],
                       filter(lambda x: is_not_empty(x[1]), sentiment_tuples))
sentiment_tuples = flat_map_values(sentiment_tuples)
sentiment_tuples = map(lambda s: [s[1], s[0]], sentiment_tuples)
group_by_candidates = [(key, sum(1 for _ in group)) for key, group in
                       groupby(sorted(sentiment_tuples, key=get_key), get_key)]

print "Generating Full DataHolder"
full_data = DataHolder(candidates, sentiment_tuples)

print "Generating Equal Tweets DataHolder"
minimum = get_value(min(group_by_candidates, key=get_value))
equal_tweets = [item for items in [list(group)[:minimum] for key, group in groupby(sorted(sentiment_tuples), key=get_key)] for item in items]

equal_data = DataHolder(candidates, equal_tweets)
# print "Generating Equal Tweets Second Round DataHolder"
# equal_data_second_round = DataHolder(candidates_second_round, equal_tweets)

print "Generating plots ..."
PlotGenerator("todos-tweets-para-todos-candidatos", full_data).plot()

PlotGenerator("quantidade-de-tweets-iguais-para-todos-candidatos", equal_data).plot()

# PlotGenerator("quantidade-de-tweets-iguais-para-candidatos-do-segundo-turno", equal_data_second_round).plot()
