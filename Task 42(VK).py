def print_christmas_tree(N : int) -> str:
    last_tier = 1 + 2 * (N - 1)
    
    current_tier = 1
    
    string_with_tree = ''
    
    for i in range(N):
        string_with_tree += ' ' * int(((last_tier - current_tier) / 2))
        string_with_tree +=  '*' * current_tier 
        string_with_tree += ' ' * int(((last_tier - current_tier) / 2)) +'\n'
        current_tier += 2
        
    print(string_with_tree)    

print_christmas_tree(5)

print(end='')

print_christmas_tree(7) 
