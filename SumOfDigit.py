n = int(input("enter a digit:"))
sum =0
while(n!=0):

    ld= n%10 
    n= n%1
    sum += ld  
    print("the sum of digit is",sum)
    break

    