from pydantic import BaseModel

class Course(BaseModel):
    name: str
    note: str
    students: int


data = {
    "name": "Couse Two",
    "note": "Dummy note",
    "students": 10
}
c = Course.model_validate(data)

print(c)