rental_car = input("What kind of rental car you would like ? ")

lower_rental_car = rental_car.lower()

if lower_rental_car == "sabaru":
    message = "Let me see if I can find you a Sabaru"
elif lower_rental_car == "ford":
    message = "Let me see if I can find you a Ford"
elif lower_rental_car == "tesla":
    message = "Let me see if I can find you a Tesla"
else :
     message = "I'm sorry, we don't have that car available for rent."

print(message)