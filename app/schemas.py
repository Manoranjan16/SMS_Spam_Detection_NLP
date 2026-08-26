from pydantic import BaseModel

class SpamRequest(BaseModel):
    message: str

class SPamResponse(BaseModel):
    message: str
    prediction: str

    