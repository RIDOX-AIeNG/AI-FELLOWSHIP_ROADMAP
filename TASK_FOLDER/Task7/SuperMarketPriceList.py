supermarket_pricelist = {} 
items = ["Maggi","Sugar", "salt", "Spoon", "milk"]
Maggi_price = float(input("Enter the price: "))
Sugar_price = float(input("Enter the price: "))
salt_price = float(input("Enter the price: "))
spoon_price = float(input("Enter the price: "))
Milk_price = float(input("Enter the price: "))
print(f"Bread: {Maggi_price}")
print(f"Burger: {Sugar_price}")
print(f"rice: {salt_price}")
print(f"garri: {spoon_price}")
print(f"Milk: {Milk_price}")
print("\nAvailable Items: ", list(supermarket_pricelist.keys()))
items_to_update = input("Enter item to be updated :")
while items_to_update not in supermarket_pricelist:
    print("item not available,select from:", list(supermarket_pricelist.keys()))
    items_to_update = input("Enter item to be updated :")
new_price = input(f" Enter new price {items_to_update}:")
supermarket_pricelist.update({items_to_update:new_price})
print("\nUpdated pricelist:")
for item,price in supermarket_pricelist.items():
    print(f"{item}:{price}")