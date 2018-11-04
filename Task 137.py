def main(N):
    i = 2
    dels = list()
    while i < 10:
        if N % i == 0:
            N /= i
            dels.append(i)
        else:
            i += 1        
    if N != 1:
        return -1
    else:
        string = ''
        for i in sorted(dels):
            string += str(i)
        return string    

print(main(11))
print(main(14))    
