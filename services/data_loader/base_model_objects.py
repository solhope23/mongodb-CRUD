from pydantic import BaseModel
import uvicorn

class Soldier(BaseModel):

    soldier_ID : int
    first_name : str
    last_name : str
    phone_number : int
    rank : str

class UpdateSoldierField(BaseModel):

    soldier_ID : int
    field : str
    value : str

class DeleteSoldier(BaseModel):

    soldier_ID: int



