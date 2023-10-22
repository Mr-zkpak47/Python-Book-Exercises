pet_1 = {
    "kind" : "Cat",
    "owner" : "Shaqas",
}

pet_2= {
    "kind" : "Dog",
    "owner" : "Qasim",
}

pet_3 = {
    "kind" : "Rabbit",
    "owner" : "Hammad",
}

pets = [pet_1, pet_2, pet_3];

for pet in pets : 
    print(f"Kind of Animal : {pet["kind"]}")
    print(f"Owner of Animal : {pet["owner"]}")