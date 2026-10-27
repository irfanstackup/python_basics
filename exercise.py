operator=input("enter the operator ")
num1=int(input("enter the first no"))
num2=int(input("enter the second number"))
if operator=="+":
    print("the sum is ",num1+num2)
elif operator=="-":
    print("the difference is", num1-num2)
elif operator=="*":
    print("the product is ", num1*num2)
elif operator=="/":
    print("the remainder is", num1/num2)
else:
    print("the operator is not found")

