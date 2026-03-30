person = {
    "name": "Johny",
    "age": 36,
    "city": "Shand"
}

print("name:", person["name"])
print("age", person["age"])

person["Job"] = "Engineer"
print("Updated dictionary:", person)

names = ["Nara", "Mateve", "Boogii"]
names.sort()
print(names)
print(names[0:2])
print(names[1:3])

student = {"nara": "sara", "grades": {"math": 90, "english": 85}}
print(student["grades"]["english"])

people = [
    {"name": "sara", "age": 25},
    {"name": "tse", "age": 30}
]

for person in people:
    print(person["name"], "is", person["age"], "years old")

person = {"name": "sara", "age": 28, "city": "darkhan"}
print(person["name"])
print(person["age"])
print(person["city"])
person["age"] = 41
print(person["age"])
person["job"] = "engineer"
print(person["job"])

student = {
    "name": "Tse",
    "grades": {"math": 91, "english": 89}
}

print(student["grades"]["math"])