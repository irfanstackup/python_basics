import sub
x=int(input("enter the first no"))
y=int(input("enter second no"))
print()

result=sub.add(x,y)
print("the sum is",result)
print(",,,,,,,,,,,,,,,,,,,,,,,,")

result=sub.sub(x,y)
print("the diff is",result)
print(",,,,,,,,,,,,,,,,,,,,,,,,,")
result=sub.mul(x,y)
print("the product is",result)

print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
result=sub.div(x,y)
print("the qoutient",result)
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
result=sub.rem(x,y)
print("the remainder is",result)
print("................................")