# Store inventory Update.

store = {"Book": 10, "Pen": 20, "Bag": 5}
item_to_buy = input("Enter item: ")
Quantity = input("Enter quantity: ")
print("Before Purchase: ", store)
store[item_to_buy] -= Quantity
print("After purchase: ", store)