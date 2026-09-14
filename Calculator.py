a = int(input("Enter the value of a :"));
b = int(input("Enter the value of b : "));
method = int(input('''Enter the method : 
1. sum 
2. multiply              
3. subtraction
-: '''))
               
if (method==1) :
    print(f"{a}+{b}={a+b}");
elif(method ==2 ) :
    print(f"{a}x{b}={a*b}");
else : 
    print(f"{a}-{b}={a-b}");
