from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbEmbed"]
artist_collection = db["ArtistsTracks"]

out = artist_collection.aggregate([
    {
        "$unwind": "$tracks"
    },
    {
        "$match": {
            "tracks.track_id": {
                "$regex": '^70',
                "$options": 'm'
            }
        }
    },
    {
        "$group": {
            "_id": '',
            "avg_danceability": {
                "$avg": "$tracks.danceability"
            }
        }
    }
])

for x in out:
    print(x)
