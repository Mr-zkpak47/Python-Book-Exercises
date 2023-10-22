person_1 = {
    "first_name" : "John",
    "last_name" : "Doe",
    "age" : 21,
    "city" : "London"
}
person_2 = {
    "first_name" : "Smith",
    "last_name" : "Emmerson",
    "age" : 31,
    "city" : "Tokyo"
}
person_3 = {
    "first_name" : "Hammad",
    "last_name" : "Khan",
    "age" : 15,
    "city" : "Karachi"
}

people = [person_1,person_2,person_3]

for person in people:
    print(f"First Name : {person["first_name"]}")
    print(f"Last Name : {person["last_name"]}")
    print(f"Age : {person["age"]}")
    print(f"City : {person["city"]}")