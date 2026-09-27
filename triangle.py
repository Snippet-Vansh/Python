side1  = int(input("enter the side 1 : "))
side2 = int(input("enter the side  2 :"))
side3 = int(input("enter the side  3 :"))
if side1 == side2 and side2 == side3 and side3 == side1 :
    print("triangle is equilateral")
elif side1 == side2 or side2 == side3 and side3 != side1 :
    print("triangle is isoceles")
elif side1 != side2 and side2 != side3 and side3 != side1 :
    print("trinagle is scaler")        