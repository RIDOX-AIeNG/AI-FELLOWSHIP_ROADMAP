favorite_food1 = input("enter favorite dish: ")
favorite_food2 = input("enter favorite dish: ")
favorite_food3 = input("enter favorite dish: ")
dishes = []
dishes.append(favorite_food1)
dishes.append(favorite_food2)
dishes.append(favorite_food3)
print(tuple(dishes))
print("\n".join(dishes))