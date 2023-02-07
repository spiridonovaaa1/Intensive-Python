n=int(input())
dig3=n % 10
dig2=(n // 10) % 10
dig1=n // 100
print(dig1, dig2, dig3, sep=',')