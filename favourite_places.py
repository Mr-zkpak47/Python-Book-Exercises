favourite_places = {
    "Hammad": ["Harte", "Hollywood", "Tokyo"],
    "Qasim": ["Saudi Arabia", "Turkey", "Iran"],
    "Shaqas": ["Germany", "France", "UK"],
}

for person,places in favourite_places.items() : 
    print(f"\n{person}'s favourite places : ")
    for place in places :
        print(f"\t{place}")