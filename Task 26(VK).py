def meanOfColumns(matrix : list) -> list:
    len_of_row = len(matrix[0])
    
    means = list()

    for j in range(len(matrix)):
        sum = 0
        for i in range(len_of_row):
            sum += matrix[i][j]
                    
        means.append(sum / len_of_row)
        
    return means

print(meanOfColumns([[2, 4, 10], [4, 4, 5], [15, 1, 9]]))  
