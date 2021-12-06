from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbEmbed"]
artist_collection = db["ArtistsTracks"]

out = artist_collection.aggregate([
    {
        '$project': {
            "_id": '$artist_id',
            'total_length': {
                '$sum': '$tracks.duration'
            },
            'artist_id': '$artist_id',
        }
    },
    {
        '$match': {
            'total_length': {
                '$ne': 0
            }
        }
    },

])

for x in out:
    print(x)
