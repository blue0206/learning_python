current_users = ['john', 'sam', 'sara', 'luke', 'rudy', 'Sylph', 'joey', 'ken']
new_users = ['John', 'kenny', 'carl', 'rudY', 'ben', 'martin', 'sAra', 'will']

copy_current = [copy.lower() for copy in current_users]

if new_users:
    for user in new_users:
        if user.lower() in copy_current:
            print(f"Sorry! {user} is not available. Kindly enter a new username.")
        else:
            print(f"{user} is available!")
else:
    print("Please enter a username!")