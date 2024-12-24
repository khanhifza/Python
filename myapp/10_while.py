print('enter a number  to check if it EVEN or not')
user_input=""
while user_input!= 'q':  
    user_input=int(input('enter a no. and q for quit - '))
    if user_input.isdigit():
      if user_input % 2==0:
        print('yes,no. is EVEN')
    else:
      print('No. is ODD') 
     
        
    
        
   
