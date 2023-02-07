y1 = int(input()) #год рождения
m1 = int(input()) #месяц рождения
y2 = int(input()) #наступишвий год
m2 = int(input())
x=((y2 - y1) * 12 + m2 - m1) // 12
print(x)