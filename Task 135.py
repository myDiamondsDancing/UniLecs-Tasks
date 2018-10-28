from math import ceil

def main(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 1
    elif N == 3: 
        return 2
    else:
        count = 3
        for i in range(ceil(N / 2), N - 2):
            count += main(N - i) 
        return count 

for i in (5, 7, 9, 11, 100):
    print(main(i))  
