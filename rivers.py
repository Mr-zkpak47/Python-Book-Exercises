rivers: dict[str, str] = {"Nile": "Egypt", "Amazon": "Brazil", "Yangtze": "China"}

for river, city in rivers.items():
    print(f"The {river} runs through {city}")

for river in rivers.keys():
    print(river)

for city in rivers.values():
    print(city)