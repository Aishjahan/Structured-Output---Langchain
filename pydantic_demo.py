from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10 , default=8, description='A decimal value representing cgpa of a student')

new_student = {'name' : 'aish', 'age' : '67', 'email' : 'ais@gmail.com', 'cgpa' : 5} # apne aap se values ka type change kar deta to match the schema if possible

student = Student(**new_student)

print(type(student))
print(student)