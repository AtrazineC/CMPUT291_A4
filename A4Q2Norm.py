from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbNorm"]
track_collection = db["Tracks"]

out = track_collection.aggregate([
    {
        "$match": {
            "track_id": {
                "$regex": '^70',
                "$options": 'm'
            }
        }
    },
    {
        "$group": {
            "_id": '',
            "avg_danceability": {
                "$avg": "$danceability"
            }
        }
    },
])

for x in out:
    print(x)
