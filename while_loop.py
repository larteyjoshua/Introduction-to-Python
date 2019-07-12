"""i=0
while(i<10):
    i = i + 1
    print(i)
    
    print(" ")
    
i=6
while(i<19):
    i = i + 1
    print(i)
    print(" ")
    
i=12
while(i<21):
    i = i + 2
    print(i)
    print(" ")
     
def even_number():
    a= int(input("Please Enter the first number"))
    b= int(input("Please enter the second number"))     
    i=a
    while(i<b):
        i= i+1
        if (i%2)==0:
            print(i) 
           
even_number()"""

def reverse_even():
    a= int(input("Please Enter the first number "))
    b= int(input("Please enter the second number less than the first one "))     
    i=a
    while(i>b):
        i= i-1
        if (i%2)==0:
             print(i) 
    
           
reverse_even()


