from pydantic import BaseModel, Field

class SpamRequest(BaseModel):
    message: str = Field(..., min_length=1)

class SPamResponse(BaseModel):
    message: str
    prediction: str

