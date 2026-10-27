#syntax for list compression: [expression for value in itterable if condition]
# print([x*2 for x in range(1,11)])


# triples=[y*3 for y in range(1,11)]
# print(triples)

# square=[x*x for x in range(1,11)]
# print(square)

# double=[]   # normal list method
# for x in range(1,11):
#     double.append(x*2)
# print(double)

# cars=["xuv","verna","fronx","mini"]
# cars=[car.upper() for car in cars]
# print(cars)
# print([car[0] for car in cars])

# numbers=[1,-2,3,-4,5,6,-7]
# positive_no=[num for num in numbers if num>0]
# negative_no=[nums for nums in numbers if nums<0]
# print(positive_no)
# print(negative_no)

# even_no=[num for num in range(1,11) if num%2==0]
# odd_no=[nums for nums in range(1,11) if nums%2==1]
# print(even_no)
# print(odd_no)

number=[30,40,50,20,55,22,60]
passed=[num for num in number if num>=30]
failed=[nums for nums in number if nums<30]
print("passed students",passed)
print("failed students",failed)


