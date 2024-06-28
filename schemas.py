from pydantic import BaseModel, field_validator
from typing import List


class Child(BaseModel):
    name: str
    last_name: str
    age: int


class Person(BaseModel):
    name: str
    age: int
    childrens: List[Child]

    @field_validator('name')
    def check_name(cls, name):
        if 2 < len(name) < 15:
            return name
        else:
            raise ValueError('name length have to be in range [2 - 15]')

