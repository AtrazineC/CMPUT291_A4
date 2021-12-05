from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
# Connect to the default port on localhost for the mongodb server.
# client = MongoClient()


# Create or open the video_store database on server.
db = client["A4dbEmbed"]

# List collection names.
collist = db.list_collection_names()
if "movies_collection" in collist:
    print("The collection exists.")

# Create or open the collection in the db
artist_collection = db["ArtistsTracks"]

# delete all previous entries in the movies_collection
# specify no condition.
artist_collection.delete_many({})

with open('artists.json', encoding='utf-8') as f:
    artists = loads(f.read())

ret = artist_collection.insert_many(artists)

# Print list of the _id values of the inserted documents
movie_ids = ret.inserted_ids
print(movie_ids)

# Insert members into a new collection.
track_collection = db["Tracks"]

# delete previous docs in the members collection.
track_collection.delete_many({})

with open('tracks.json', encoding='utf-8') as f:
    tracks = loads(f.read())

ret = track_collection.insert_many(tracks)

print(ret.inserted_ids)

artist_collection.update_many(
    {},
    {'$rename': {'tracks': 'trackids'}},
)

artist_collection.update_many(
    {},
    {'$set': {'tracks': []}},
)

for x in range(1569):
    track = track_collection.find_one_and_delete({})
    print(track)

    print(track_collection.count_documents({}))

    artist_collection.update_many(
        {'trackids': track.get("track_id")},
        {'$push': {'tracks': track}},
        upsert=True
    )

artist_collection.update_many(
    {},
    {'$unset': {'trackids': ""}}
)

# artist_collection.rename('ArtistsTracks')
track_collection.drop()
