sandwich_orders: list[str] = [
    "tuna",
    "pastrami",
    "turkey",
    "pastrami",
    "veggie",
    "ham",
    "pastrami",
    "chicken",
    "pastrami",
]

finished_sandwiches:list[str] = []

for sandwich in sandwich_orders : 
    if sandwich == "pastrami":
        sandwich_orders.remove("pastrami")

while sandwich_orders : 
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwich.")
    finished_sandwiches.append(finished_sandwich)

print("\nFinished Sandwiches : ")

for finished_sandwich in finished_sandwiches : 
    print(f"{finished_sandwich}")