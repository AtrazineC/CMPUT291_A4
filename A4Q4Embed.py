import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
# Connect to the default port on localhost for the mongodb server.
# client = MongoClient()

db = client["A4dbEmbed"]

artist_collection = db["ArtistsTracks"]

out = artist_collection.aggregate([{'$match': {'tracks.release_date': {'$gt': datetime.datetime(1950, 1, 1, 0, 0)}}},
                                   {'$unwind': '$tracks'},
                                   {'$project': {'name': 1,
                                                 't_name': '$tracks.name',
                                                 't_release_date': '$tracks.release_date'}},
                                   {'$sort': {'t_release_date': 1}}
                                   ])

for x in out:
    print(x)
