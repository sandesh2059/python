accounts = {"admin": "admin123", "user1": "pass111"}
accounts["teacher"] = "teach883"
accounts["user2"] = "pass222"
print(accounts)

input_user = input("Enter user: ")
input_pass = input("Enter pass: ")

if input_user in accounts and accounts[input_user] == input_pass:
    print("access granted")
else:
    print("not recognized")