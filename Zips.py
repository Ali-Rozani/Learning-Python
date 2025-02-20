# A zip can also be called iterables
Usernames = ["Mister", "Guest"]
Passwords = ["mister46cold", "p@$$w0rd"]
Users = zip(Usernames, Passwords)
for i in Users:
    print(i)