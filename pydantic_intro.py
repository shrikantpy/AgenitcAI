
from pydantic import BaseModel


from dataclasses import dataclass
@dataclass
class Person():
    name:str
    age:int
    city:str

person = Person(name="Shrikant", age=40, city="Bangalore")
print(person)

class Person(BaseModel):
    name:str
    age:int
    city:str

person = Person(name="Shrikant", age=40, city="Bangalore")
print(person)

#person1 = Person(name="Shrikant", age="forty", city="Bangalore-56")
#print(person1)


# Model with optional fields:
# We can add optional field using Python's optional type.

from typing import Optional
class Employee_Opt(BaseModel):
    name:str
    age:int
    dept:str
    city: Optional[str] = "Bangalore" #optional with default value
    salary: Optional[int] = None # Optional with default value as null
    isActive: Optional[bool] = True #optional with default boolean value

person = Employee_Opt(name="Shrikant", age=40, dept="Engineering")
print(person)



# Definition:
# - Optional[type]: Indicates the field can be None
# - Default value (= None or = True): Makes the field optional
# - Required fields must still be provided
# - Pydantic validates types even for optional fields when values are provided

from typing import List
# from typing import Dict

class Classroom(BaseModel):
    room_number: str
    students: List[str] # List of strings
    capacity: int

# Create inherited classroom
classroom = Classroom(room_number='B204', students=["Ramesh", "Suresh", "Govind", "Shambhavi"], capacity=15)
print(classroom)

try:
    classroom = Classroom(room_number="B78", students="Suresh", capacity=50)
except Exception as e:
    print(e)

# Model with Nested Models
# Create complex structures with nested models:

class student_score(BaseModel):
    maths: int
    physics: int
    chemestry: int
    biology: int

class student_detail(BaseModel):
    name: str
    roll_num: str
    score: student_score     # Nested base model

# Creating student with nested details

student = student_detail(name="Ramesh", roll_num="A23", score={"maths": 96, "physics": 92, "chemestry": 93, "biology":95})
print(student)

# Below one will throw an error during score validation
# student = student_detail(name="Ramesh", roll_num="A23", score={"maths": 96, "physics": "Hello", "chemestry": 93, "biology":95})
# print(student)


# Below one will not throw an error during score validation because model takes care of automatic type casting.
student = student_detail(name="Ramesh", roll_num="A23", score={"maths": 98, "physics": "97", "chemestry": 94, "biology":95})
print(student)


# Pydantic Fields: Customization and Constraints

#The Field function in Pydantic enhances model fields beyond basic type hints by allowing you to specify validation rules,
# default values, aliases, and more. Here's a comprehensive tutorial with examples.
