def permutation(string :str) -> list:
    values = [ a + b + c + d
            for a in string
            for b in string
            for c in string
            for d in string
            if ( a != b and b != c and a != c and a != d and b != d and c != d)
            ]
    return sorted(values)
    
def main(string : str):
    perm = permutation(string)
    
    try:
        return perm[perm.index(string) + 1]
    except IndexError:
        return 'This is impossible'
    
print(main('dcba'))
print(main('word'))   
