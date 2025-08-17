#Supermarket Price list
#Create a dictionary that stores the items and their prices.
#Create a function that allow users to enter and update the prices.
item = {} 
item1 = ("Maggi")
item2 = ("Sugar")
item3 = ("salt")
item4 = ("spoon")
item5 = ("Milk")
sup = (item1,item2,item3,item4,item5)
for key in item:
    print(key)
price={}
Maggi_price = input("Enter the price: ")
Sugar_price = input("Enter the price: ")
salt_price = input("Enter the price: ")
spoon_price = input("Enter the price: ")
Milk_price = input("Enter the price: ")
price = {Maggi_price,Sugar_price,salt_price,spoon_price,Milk_price}
print(f"\nAvailable Items and their prices:\n{item1}: #{Maggi_price}\n{item2}: #{Sugar_price}\n{item3}: #{salt_price}\n{item4}: #{spoon_price}\n{item5}: #{Milk_price}\n")
updatedprice = input("Enter the new price of Maggi: #")
price.update(updatedprice)
Maggi_price = updatedprice
print(f"The new price of Maggi is: #{updatedprice}")
print("\nThe new price list for each items are:")
print(f"{item1}: #{updatedprice}\n{item2}: #{Sugar_price}\n{item3}: #{salt_price}\n{item4}: #{spoon_price}\n{item5}: #{Milk_price}\n")

