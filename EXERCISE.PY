menu={"normal mandi": 200,
      "spicy mandi":250,
      "alfaham mandi":300,
      "periperi":310,
      "mexican alfaham":330}
print("..................menu.....................")

cart=[]
total=0
for key,values in menu.items():
    print(key,":",values)
    print("/////////////////////////////")

while True:
    food=input("enter the food  you like and(q to quit)" )
    if food.lower()=="q":
        print("your oder is taken")
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
    print()
print("your total ammt is" ,total)