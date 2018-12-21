def main(N : int) -> list:
    mask = [1] * (N - 1)
    numbers = list()
    
    for i in range(2, int(N / 2)):
        t = 2 * i
        
        while t <= N:
            mask[t - 2] = 0
            t += i    

    for i in range(len(mask)):
        if  mask[i] != 0:
            numbers.append(i + 2)
            
    return numbers        
            
            
for i in (5, 26, 38, 41):
    print(main(i))
    
