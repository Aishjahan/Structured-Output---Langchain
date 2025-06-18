from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
new_person : Person = {'name' : 'aish', 'age' : 22}

print(new_person)