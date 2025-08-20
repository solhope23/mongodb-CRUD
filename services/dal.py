import os
from typing import List, Dict, Any
from pymongo import MongoClient, errors
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI", "localhost:27017")
DB_NAME = os.getenv("DB_NAME", "enemy_soldiers")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "soldier_details")

ALLOWED_FIELDS = {"first_name", "last_name", "phone_number", "rank"}

class DAL:

    def __init__(self, uri: str = MONGODB_URI, db_name: str = DB_NAME, collection: str = COLLECTION_NAME):
        if not uri:
            raise ValueError("Missing MONGODB_URI")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.col = self.db[collection]
        self.col.create_index("soldier_id", unique=True)


    def close(self) -> None:
        self.client.close()


    def read_all(self) -> List[Dict[str, Any]]:
        cursor = self.col.find({}, {"_id": 0})
        return list(cursor)




