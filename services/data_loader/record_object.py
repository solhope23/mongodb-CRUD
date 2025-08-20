from pydantic import BaseModel

class RecordObject(BaseModel):
    ID: int
    first_name : str
    last_name : str
    phone_number : int
    rank : str

