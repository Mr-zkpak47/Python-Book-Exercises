my_pizzas = ["Fajita", "Pepporina", "Chicken Tikka"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Hawaiian Pizza")
friend_pizzas.append("Buffalo Pizza")
print("My favourite pizzas : ")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favourite pizzas : ")
for pizza in friend_pizzas:
    print(pizza)