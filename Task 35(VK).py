def main(a : str, b : str) -> int:
    if len(a) > len(b):
        return a
    elif len(b) > len(a):
        return b
    else:
        for i in range(len(a)):
            if a[i] > b[i]:
                return a
            elif b[i] > a[i]:
                return b
    return a 

print(main('123', '265464'))    
