responses: dict[str, str] = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) : ")

    if repeat == "no":
        polling_active = False

for name,mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain}")