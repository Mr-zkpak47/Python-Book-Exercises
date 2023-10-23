toppings = "";
message = ""
while message != "quit" :
    message = input("Enter toppings or type quit to break the loop : ")
    if message != "quit" :
        print(f"The {message} is adding to the pizza.")