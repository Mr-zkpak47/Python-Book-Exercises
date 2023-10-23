sandwich_orders: list[str] = [
    "tuna",
    "pastrami",
    "turkey",
    "veggie",
    "ham",
    "pastrami",
    "chicken",
    "pastrami",
]

finished_sandwiches:list[str] = []

while sandwich_orders : 
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwich.")
    finished_sandwiches.append(finished_sandwich)

print("\nFinished Sandwiches : ")

for finished_sandwich in finished_sandwiches : 
    print(f"{finished_sandwich}")