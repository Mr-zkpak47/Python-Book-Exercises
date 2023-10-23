dream_vacations:list[str] = []
count = 1;

while True :
    response = input("If you could visit one place in the world, where would you go? (Type 'quit' to end):")
    if response.lower() == "quit":
        break;
    dream_vacations.append(response)

print("\n--- Poll Results ---")
for dream_vacation in dream_vacations : 
    print(f"{count}. {dream_vacation}")
    count += 1
