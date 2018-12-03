def main(arr):
    max_sum = arr[0][0]
    max_el = arr[0][0]
    
    y = len(arr)
    x = len(arr[0])
    
    for i in range(y):
        for j in range(x):
            sum = 0
            
            if j + 1 < x:
                sum += arr[i][j + 1]

            if j - 1 >= 0:
                 sum += arr[i][j - 1]

            if i + 1 < y:
                 sum += arr[i + 1][j]

            if i - 1 >= 0:
                  sum += arr[i - 1][j]            

            if sum > max_sum:
                max_sum = sum             
                max_el = arr[i][j]
                
    return max_el

print(main([[1, -2, 3], [-4, 5, 6], [7, 8, -9]]))
