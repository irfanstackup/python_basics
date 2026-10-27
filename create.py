# f1=open("game.txt","x")# x mode is used to create a file
# f2=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\game.txt","r")
# print(f2.read())

# f3=open("sam.txt","x")
# f4=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\sam.txt","r")
# print(f4.read())

# f5=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\sam.txt","w")
# print(f5.write("your query is recorded"))# in  w mode the file gets rewritted or replaced

# f6=open(("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\sam.txt","a"))
# print(f6.append())

# f5=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\sam.txt","w")
# print(f5.write("how lonley are you"))

# f6=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\sam.txt","r+")
# print(f6.read()) #in r+ mode the file is not overwrited instead the write function adds the text into the file instead of replacing or rewritting
# f6.seek(0)# we use seek function so thtat the contents get replaced
# f6.write("i can fix that")

# f1=open("salih.txt","x")
# f2=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\salih.txt","w+")
# f2.write("but salih is afriend of ashlin")
# f2.seek(0)

# print(f2.read())

# f2=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\salih.txt","a")
# f2.write("but salihs girlfriend is priya")

# f3=open("jee.txt","a") # a can be used to create and open a file and to append data with write
# f3=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\jee.txt","a")
# f3.write("its a need dawn")

# f3=open("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\jee.txt","a+")      
# f3.seek(0) #a+ is used to read then append so we use seek first to 0 so it reads from starting and then apeends after reading
# print(f3.read())
# f3.write("its a new life")

#import os
# os.rename("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\\salih.txt","hyper.txt")
#always use path 
# os.remove("C:\\Users\\Nazeer\\Desktop\\python basics\\file_handling\game.txt"
