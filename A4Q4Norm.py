import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbNorm"]
artist_collection = db["Artists"]
track_collection = db["Tracks"]

out = track_collection.aggregate([
    {
        '$match': {
            'release_date': {
                '$gt': datetime.datetime(1950, 1, 1, 0, 0)
            }
        }
    },
    {
        '$unwind': '$artist_ids'
    },
    {
        '$lookup': {
            'localField': 'artist_ids',
            'from': 'Artists',
            'foreignField': 'artist_id',
            'as': 'ArtistsNames'
        }
    },
    {
        '$unwind': '$ArtistsNames'
    },
    {
        '$project': {
            'name': '$ArtistsNames.name',
            't_name': '$name',
            't_release_date': '$release_date'
        }
    },
    {
        '$sort': {
            't_release_date': 1
        }
    }
])

for x in out:
    print(x)
