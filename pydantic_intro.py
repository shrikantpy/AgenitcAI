
from pydantic import BaseModel


from dataclasses import dataclass
@dataclass
class Person():
    name:str
    age:int
    city:str

person = Person(name="Shrkant", age=40, city="Bangalore")
print(person)

class Person(BaseModel):
    name:str
    age:int
    city:str

person = Person(name="Shrkant", age=40, city="Bangalore")
print(person)

#person1 = Person(name="Shrkant", age="forty", city="Bangalore-56")
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
