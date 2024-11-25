from pydantic import BaseModel


class Course(BaseModel):
    name: str | None = None
    title: str
    total_students: int
    id: list[int] = []



c = Course(title='Title One', total_students= 10)

print(c)