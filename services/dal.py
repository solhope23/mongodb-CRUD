import os
from typing import List, Dict, Any
from pymongo import MongoClient, errors
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "data")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "people")

ALLOWED_FIELDS = {"first_name", "last_name", "phone_number", "rank"}

class DAL:

    def __init__(self, uri: str = MONGODB_URI, db_name: str = DB_NAME, collection: str = COLLECTION_NAME):
        if not uri:
            raise ValueError("Missing MONGODB_URI")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.col = self.db[collection]
        self.col.create_index("id", unique=True)


    def close(self) -> None:
        self.client.close()


