from math import ceil

def main(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    elif N == 2:
        return 1
    elif N == 3: 
        return 2
    elif N == 4:
        return 2    
    else:
        count = 0
        for i in range(ceil(N / 2), N + 1):
            count += main(N - i) 
        return count 

print(main(11))
