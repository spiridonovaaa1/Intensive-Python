x=int(input())
if x>99: 
    print("Ввод двузначного числа, десятки")
else:
    print(x//10)
y=int(input())
if y>99: 
    print("Ввод двузначного числа, единицы")
else:
    print(y%10)