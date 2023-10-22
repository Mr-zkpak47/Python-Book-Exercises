favourite_numbers = {
    "Harry": [i for i in range(0, 5)],
    "Hammad": [i for i in range(5, 10)],
    "Shaqas": [i for i in range(10, 15)],
    "Qasim": [i for i in range(15, 20)],
    "Moiz": [i for i in range(20, 25)],
}

for key, values in favourite_numbers.items():
    print(f"\n{key}'s favorite number is : ")
    for value in values:
        print(f"\t{value}")
