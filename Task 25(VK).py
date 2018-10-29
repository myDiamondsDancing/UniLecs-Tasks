def pow(x, y):
    x1 = 1
    for y in range(y):
        x1 *= x
    return x1 

for x, y in ((2, 3), (3, 4), (5,2), (6, 3)):
    print(pow(x, y)) 
