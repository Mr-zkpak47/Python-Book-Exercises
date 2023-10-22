current_users = ["Harry","Hammad","Qasim","Shaqas","Moiz"]
new_users = ["Harry","zohaib","qasim","Arham","Moiz"]
lower_current_users = [user.lower() for user in current_users]

for new_user in new_users : 
    lower_new_user = new_user.lower()
    if lower_new_user in lower_current_users : 
        print(f"Username '{new_user}' is not available.")
    else:
        print(f"Username '{new_user}' is available.")