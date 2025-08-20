import os
from typing import List, Dict, Any
from pymongo import MongoClient, errors


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

    def write(self, soldier_id: int, first_name: str, last_name: str, phone_number: str, rank: str) -> bool:
        doc = {
            "soldier_id": soldier_id,
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "phone_number": phone_number.strip(),
            "rank": rank.strip(),
        }
        try:
            result = self.col.insert_one(doc)
            print(f"Insert successful, inserted_id: {result.inserted_id}")
            return True
        except errors.DuplicateKeyError as e:
            print(f"Duplicate key error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False



    def update(self, soldier_id: int, field: str, value: str) -> bool:
        if field not in ALLOWED_FIELDS:
            return False
        res = self.col.update_one({"soldier_id": soldier_id}, {"$set": {field: value.strip()}})
        return res.matched_count == 1


