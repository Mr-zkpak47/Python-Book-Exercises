usernames:list = ['Harry']

if not(usernames) :
    print("We need to find some users.")
else:
    for username in usernames:
        if username.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        elif username.lower() != "admin":
            print(f"Hello {username}, thank you for logging in again.")
