from typing import Annotated

from pydantic import BaseModel, Field ,ConfigDict

class UserCreate (BaseModel):
    student_id: int = Field(le =0)

    equipment_id: int = Field(le = 0)

    description: str = Field (min_lenght= 5 , max_lenght = 100 )


class UserRead(BaseModel):
    model_config = ConfigDict(
        from_attributes= True
    )
    id: int
    equipment_id = int 
    description = str
    student_id = str



class IdRead (UserCreate):
    id: int 
    model_config= ConfigDict(
        from_attributes= True
    )