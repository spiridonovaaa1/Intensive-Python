v1 = float(input()) #km/h
v2 = float(input()) #m/s
if v1 < v2 * 1000 / 3600:
    print("v1 faster")
else:
    print("v2 faster")

