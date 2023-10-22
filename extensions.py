# Create an extended dictionary of favorite places
favorite_places = {
    "Alice": ["Paris", "New York", "Sydney"],
    "Bob": ["Tokyo", "Hawaii"],
    "Charlie": ["London"],
    "David": ["Barcelona", "San Francisco", "Kyoto"],
    "Eve": ["Rome", "Cape Town"]
}

# Loop through the dictionary and print each person's name and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for i, place in enumerate(places, start=1):
        print(f"{i}. {place}")
    print()

