# Assignment 4: Inventory Management (Intermediate → Advanced)
# Task
# Create an inventory dictionary.
# inventory = {
#     "pen": 10,
#     "book": 5,
#     "eraser": 0
# }
# Steps
# Choose an item.
# Check:
# If the item exists
# If quantity > 0
# Reduce quantity by 1 if available.
# Print appropriate messages:
# "Item Purchased"
# "Out of Stock"
# "Item Not Found"

inventory = {
    "pen": 10,
    "book": 5,
    "eraser": 0
}
print(inventory)

item = input("enter a item you want to purchase: ") 

if item in inventory and inventory[item] > 0:
    print("item purchased")
    inventory[item] = inventory[item] - 1
    print(inventory)
elif item in inventory and inventory[item] <=0:
    print("out of stock")
else:
    print("item not available")
