# with open("user.txt", "w") as file:
#     file.write("this is my first text file using python \n")
    
# with open("user.txt", "a") as file:
#     file.write("i am excited to complete python concept ")
    
with open("user.txt", "r") as file:
    content= file.readlines()
for name in content:    
 print(name.rstrip())
   