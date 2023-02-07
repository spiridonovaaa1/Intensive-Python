import math
r=int(input()) #радиус круга
l=int(input()) #сторона квадрата
S1= math.pi*r**2 #площадь круга
S2=l**2 #площадь квадрата
if S1>S2:
    print(S1, "больше", S2)
else:
    print(S1, "меньше", S2)


