# coding=utf-8
from pymongo import MongoClient
from sentiment_analysis_utils import *
from DataHolder import DataHolder
from PlotGenerator import PlotGenerator

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
tweets = map(mapper_tweets, list(db.oldCandidateTweets.find({}, projection_tweets).limit(500)))

print "Reading Candidates"
candidates = read_candidate_mapping()
candidates = map(lambda x: (x.strip().split(",")[0], x.strip().split(",")), candidates)
candidates = flat_map_values(candidates)
candidates = set(map(lambda c: (c[1], c[0]), candidates))

print "Calculating variables from data"
full_data = DataHolder(tweets, candidates)

print "Generating plots ..."
PlotGenerator("todos-tweets-para-todos-candidatos", full_data).plot()