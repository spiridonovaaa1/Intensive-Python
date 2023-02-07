import math
S1 = int(input()) #ПЛОЩАДЬ КВАДРАТА
S2 = int(input()) #ПЛОЩАДЬ КРУГА
A = math.sqrt(S1) #сторона квадрата
R = math.sqrt(S2 / math.pi) #радиус круга
D = 2 * R
if A > D:
    print("уместится")
else:
    print("не уместится")


    
    
  
   
    


