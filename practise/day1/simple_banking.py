accounts = {
    "sandesh": 5000,
    "flins": 3000
}
print("please fill up the details")
user = input("enter the name of user: ")
withdraw = int(input("Enter the amount to withdraw: "))

if user in accounts and accounts[user] >= withdraw:
    print("amount withdrawn")
    accounts[user] = accounts[user] - withdraw
    print("remaining balance = ", accounts[user])
elif user in accounts and accounts[user] < withdraw:
    print("amount not sufficient, you have only = ", accounts[user])
else:
    print("user not found")