from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbNorm"]
track_collection = db["Tracks"]

out = track_collection.aggregate([
    {
        '$unwind': '$artist_ids'
    },
    {
        '$group': {
            "_id": '$artist_ids',
            'total_length': {
                '$sum': '$duration'
            },
        }
    },
    {
        '$match': {
            'total_length': {
                '$ne': 0
            }
        }
    },
    {
        '$project': {
            '_id': 1,
            'total_length': 1,
            'artist_id': '$_id'
        }
    },
])

for x in out:
    print(x)
