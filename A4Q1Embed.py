from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbEmbed"]
artist_collection = db["ArtistsTracks"]

out = artist_collection.aggregate([
    {
        '$project': {
            'num_tracks': {
                '$size': "$tracks"
            },
            'artist_id': 1,
            'name': 1
        }
    },
    {
        '$match': {
            'num_tracks': {
                '$gt': 0
            }
        }
    }
])

for x in out:
    print(x)
