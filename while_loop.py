# name=input("enter the users name")
# while name=="":
#     print("there is no name provided by user")
#     name=input("enter the users name")
# print("hello", name)

# age=int(input("enter the age of user"))
# while age<=0:
#     print("no records found")
#     age=int(input("enter the age of user"))

# print("the age of user is",age)


# food=input("enter your favourite food ,q to quit")
# while not food=="q":
#     print("your favourite food is ",food)
#     food=input("enter your other favourite food , q to quit")
# print("see you soon")

num=int(input("enter the users no"))
while num<1 or num>10:
    print("the number is invalid")
    num=int(input("enter the no of user again"))
print("the age of user is ",num)
    