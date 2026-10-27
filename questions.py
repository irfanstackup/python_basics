#question 1
# name=input("enter the name of the student")
# age=input("enter the age of student")
# subject1=input("enter the marks of subject 1:")
# subject2=input("enter the marks of subjectt 2:")
# subject3=input("enter the marks  of subject 3:")

# name=str(input("enter the name of the student"))
# age=int(input("enter the age of student"))
# subject1=int(input("enter the marks of subject 1:"))
# subject2=int(input("enter the marks of subjectt 2:"))
# subject3=int(input("enter the marks  of subject 3:"))

# total=subject1+subject2+subject3
# print("the total mark is",total)

# avg=(subject1+subject2+subject3)/3
# print("the average mark is",avg)

# print(type(name))
# print(type(age))
# print(type(subject1))
# print(type(subject2))
# print(type(subject3))
# print(type(total))
# print(type(avg))

# question 2
# sentence=str(input("enter the senternce"))
# print(sentence)
# print(sentence[0])
# print(sentence[-1])
# print(sentence.lower())
# print(sentence.upper())
# print(len(sentence))
# print(sentence[::-1])
# print(sentence.replace(" ","-"))

#question 3
# marks=input("enter users marks: ",)
# print(type(marks))
# marks=int(input("enter the users marks:"))
# if marks<0 or marks>100:
#     print("the marks is invalid")

# elif marks>=90:
#     print("grade A")
# elif marks>=75 and marks<=89:
#     print("grade B")
# elif marks>=50  and marks<=74:
#     print("grade C")
# elif marks<50:
#     print("fail")

# else:
#     print("enter the value of marks again")



#question 4

# n=int(input("enter the number"))
# for i in range(1,11):
#     print(i,"*",n,"=",i*n)

# i=1
# total=0
# while i<=n:
#     total=total+i
#     i=i+1
# print("sum of nos from 1 to ",n,"=",total)

# for i in range(2,n+1,2):
#     print("even nos btw 1 and", n,":",i)


#question 5
# celsius = input("Enter temperature in Celsius: ")

# print("Type before conversion:", type(celsius))

# celsius = float(celsius)

# print("Type after conversion:", type(celsius))

# fahrenheit = celsius * 9 / 5 + 32
# kelvin = celsius + 273.15

# print("Celsius:", celsius)
# print("Fahrenheit:", fahrenheit)
# print("Kelvin:", kelvin)

#question 6
# word = input("Enter a word: ")
# word = word.lower()
# if word == word[::-1]:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

# first_char = word[0]
# count = word.count(first_char)

# print("First character:", first_char)
# print("Number of times the first character appears:", count)