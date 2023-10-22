cities = {
    "New York": {
        "country": "United States",
        "population": "8.4 million",
        "fact": "The Statue of Liberty is located on Liberty Island in New York Harbor.",
    },
    "Paris": {
        "country": "France",
        "population": "2.2 million",
        "fact": "Paris is known as the 'City of Love' and is famous for the Eiffel Tower.",
    },
    "Tokyo": {
        "country": "Japan",
        "population": "13.9 million",
        "fact": "Tokyo is the largest city in Japan and has a rich cultural heritage.",
    },
}

for city,city_info in cities.items() : 
    print(f"\n{city}")
    for key,value in city_info.items():
        print(f"\t{key} : \n\t\t{value}")