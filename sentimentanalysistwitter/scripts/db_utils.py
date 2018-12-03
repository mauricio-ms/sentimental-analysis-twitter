import pprint

from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
db = client.tweetsDb


def mapper_tweets(tweet):
    return [tweet.get("id"), tweet.get("full_text"),
            map(lambda u: u.get("name"), tweet.get("userMentionEntities"))]


print "Reading Tweets ..."
projection_tweets = {"id": 1, "full_text": 1, "entities.user_mentions.name": 1, "_id": 0}

# print "Count"
# print db.oldCandidateTweets.find({}).count()

# print "Distinct"
# print db.oldCandidateTweets.distinct("id").length

print "Limit"
pprint.pprint(list(db.oldCandidateTweets.find({}, projection_tweets).limit(500)))

# print "Sort"
# pprint.pprint(list(db.oldCandidateTweets.find({}, projection_tweets).limit(500).sort("entities.user_mentions.name")))

# print "groupby"
# pprint.pprint(list(db.oldCandidateTweets.aggregate(
#     [
#         {
#             "$group": {
#                 "_id": "$entities.user_mentions.name",
#                 # "totalPrice": {"$sum": {"$multiply": ["$price", "$quantity"]}},
#                 # "averageQuantity": {"$avg": "$quantity"},
#                 "count": {"$sum": 1}
#             }
#         }
#     ]
# )))
#

print "Find eq"
pprint.pprint(len(list(
    db.oldCandidateTweets.find(
        {
            "entities.user_mentions.name": {"$eq": "Jair M. Bolsonaro"}
        }, projection_tweets
    )
)))
