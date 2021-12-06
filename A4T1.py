from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

# Create or open the video_store database on server.
db = client["A4dbNorm"]

# List collection names.
collist = db.list_collection_names()
if "movies_collection" in collist:
    print("The collection exists.")

# Create or open the collection in the db
artist_collection = db["Artists"]

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
