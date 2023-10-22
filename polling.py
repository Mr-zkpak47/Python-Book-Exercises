favourite_languages = {
    "Harry": "Python",
    "Hammad": "Javascript",
    "Shaqas": "Java",
    "Qasim": "SQL",
    "Moiz": "C#",
}

people_to_poll = ["Arham", "Moaz", "Shaqas", "Zohaib", "Qasim"]

for person in people_to_poll:
    if person in favourite_languages.keys():
        print(f"Thank you, {person}, for responding to the poll.")
    else:
        print(f"{person}, we invite you to take the favourite languages poll.")
