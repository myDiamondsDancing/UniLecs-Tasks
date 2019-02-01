def main(arr) -> list:
    map = dict()  # Hashmap
    
    for i in range(len(arr)): # for (int i = 0; i < arr.Lenght, i++){}
        map[arr[i]] = True
        
    new_arr = [0] * len(map)   #In C#, empty array
    j = 0
    
    for i in range(len(arr)):
        if map[arr[i]] is True:
            map[arr[i]] = False
            new_arr[j] = arr[i]
            j += 1 # j++
            
    return new_arr, len(new_arr)

print(main([1, 2, 3, 1, 4, 5, 5, 4, 2]))   
