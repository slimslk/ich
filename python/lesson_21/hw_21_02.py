from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])

person1 = Person(name="Alice", age="25", city="New York")
person2 = Person("Bob", "30", "London")
person3 = Person(name="Carol", age="35", city="Paris")

for person in person1, person2, person3:
    print(f"Name: {person.name}, Age: {person.age}, City: {person.city}")
