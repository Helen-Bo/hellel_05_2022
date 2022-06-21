import sys

# john = "John"
# print(sys.getsizeof(john))
# john = 12
# print(sys.getsizeof(john))
# john = 12312412412
# print(sys.getsizeof(john))

person_d = {"name": "John", "phone": "380671442543"}
print(sys.getsizeof(person_d))

john = ("John", "380671442543")
print(sys.getsizeof(john))


class Person:
    name = "John"
    phone = "380671442543"

    def get_full_data(cls) -> str:
        return f"name :{cls.name}. phone {cls.phone}"


print(sys.getsizeof(Person))

print(person_d["name"])
print(Person.name)
print(vars(Person))
