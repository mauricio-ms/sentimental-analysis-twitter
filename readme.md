python      -m pip install pandas

db.oldCandidateTweets.find({created_at: { $gte: new Date("2018-11-01T00:00:00Z") }})

db.oldCandidateTweets.find("{created_at: { $gte: new Date("2018-11-01T00:00:00Z") }}")


db.oldCandidateTweets.find({created_at: { $gte: new Date("2018-11-01T00:00:00Z") }})


db.oldCandidateTweets.find({created_at: { $lt: new Date() }})


{created_at: { $lte: new Date("11 01 2018 00:00:00 z") }}