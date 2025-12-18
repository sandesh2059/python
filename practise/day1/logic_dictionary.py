# Assignment 6: Challenge 🚀 (Logic + Dictionary)
# Task
# Create a dictionary of products with prices.

# products = {
#     "apple": 30,
#     "banana": 10,
#     "orange": 20
# }
# Steps
# Choose a product and quantity.
# Check if product exists.
# Calculate total cost.
# If total cost ≥ 100, apply 10% discount.
# Print final price.


products = {
    "apple": 30,
    "banana": 10,
    "orange": 20
}

item = input("which item do you want to purchase: ")
quantity = int(input("how much do you want to purchase: "))

if item in products and quantity > 0:
    cost = products[item] * quantity
    print("total cose: ", cost)
    if cost >= 100:
        print("providing 10% discount")
        new_cost = cost - ((10 / 100) * cost)
        print("your discounted price is: ", new_cost)
elif item in products and quantity <= 0:
    print("please enter a valid positive amount")
else:
    print("item not available")