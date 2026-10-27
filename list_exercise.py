# shoping cary
foods=[]
prices=[]
total=0

while True:
    food=input("enter the food and (q to quit) ")
    if food.lower()=="q":
        print("suceesfully completed ")
        break
    
    else:
        price=int(input("enter the price of food "))
        foods.append(food)
        prices.append(price)
for food in foods:
    print(food,end=" ")
for price in prices:
    print(price,end=" ")
    total+=price
print()
print(total)



