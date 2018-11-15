#coding=utf-8
from pymongo import MongoClient
from chart_utils import *
from sentiment_analysis_utils import *
from array_utils import *

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
tweets = map(mapper_tweets, list(db.oldCandidateTweets.find({}, projection_tweets).limit(5000)))


def log_and_calcule_sentiment(t):
    print "\n\nCandidato: {}".format(t[2])
    return [sentiment(t[1]), t[2]]


print "Calculating ..."
#sorted(sentiment_tuples, key=get_value)
#sum(map(lambda x: len(x[1]), filter(lambda x: len(x[1]) > 1, sentiment_tuples))) - 28

sentiment_tuples = map(log_and_calcule_sentiment, tweets)
sentiment_tuples = flat_map_values(sentiment_tuples)
sentiment_tuples = map(lambda s: [s[1], s[0]], sentiment_tuples)

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print "A %s is a %s." % (thing[1], key)
    print " "


# print "Group 1"
# for key, group in groupby(map(lambda x: (x[0], 1), sentiment_tuples), get_key):
#     print key
#     for item in group:
#         print item

#[(key, sum(1 for item in group)) for key, group in groupby(sorted(sentiment_tuples, key=get_key), get_key)]
# print "Group 2"
# for key, group in groupby(sorted(sentiment_tuples, key=get_key), get_key):
#     print key
#     for item in group:
#         print item

# df = pd.DataFrame(map(get_key, sentiment_tuples))
# pprint.pprint(df)
# pprint.pprint(df.groupby(0).groups)
group_by_candidates = [(key, sum(1 for item in group)) for key, group in groupby(sorted(sentiment_tuples, key=get_key), get_key)]
score_tuples = reduce_by_key(adder, map(lambda x: (x[0], x[1].get("score")), sentiment_tuples))
sentiment_tuples = reduce_by_key(concat, map(lambda x: (x[0], x[1].get("sentiments")), sentiment_tuples))

candidates = read_candidate_mapping()
candidates = map(lambda x: (x.strip().split(",")[0], x.strip().split(",")), candidates)
candidates = flat_map_values(candidates)
candidates = set(map(lambda c: (c[1], c[0]), candidates))

print "Results:"
pprint.pprint(score_tuples)
counts = join(group_by_candidates, candidates)
print "Counts:"
pprint.pprint(counts)
scores = join(score_tuples, candidates)
sentiments = join(sentiment_tuples, candidates)
# pprint.pprint(scores)

print "Plot"
plot(map(get_value, scores), map(get_key, scores), u"Score - Análise de Sentimentos")

plot(map(lambda x:  np.mean(x[1]), sentiments), map(get_key, scores), u"Média - Análise de Sentimentos")

# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#                      'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#             'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#             'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#             'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)

# print df
#
# print "groupby('Team')"
# print df.groupby('Team')
#
# print "groupby('Team') groups"
# print df.groupby('Team').groups
#
# print "groupby(['Team','Year']).groups"
# print df.groupby(['Team','Year']).groups
#
# print "mean"
# grouped = df.groupby('Year')
# print grouped['Points'].agg(np.mean)
#
# print "size"
# grouped = df.groupby('Team')
# print grouped.agg(np.size)
#
# print "sum"
# grouped = df.groupby('Team')
# print grouped.agg(np.sum)