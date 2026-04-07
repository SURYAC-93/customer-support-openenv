from pydantic import BaseModel

class Observation(BaseModel):
    ticket: str
    status: str

class Action(BaseModel):
    action_type: str   # classify / reply / close
    message: str