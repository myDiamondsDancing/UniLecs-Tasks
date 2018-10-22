def getMissedElement(arr):
    maxElement = max(arr)
    totalSum = sum(range(1, maxElement + 1))
    return totalSum - sum(arr)
    
data = {
    (1, 3, 4, 5) : 2,
    (1, 2, 3, 4, 6, 7) : 5,
    (2, 3, 4) : 1
    } 

for arr in data:
    if getMissedElement(arr) == data[arr]:
        print('Answer for {0} is {1}'.format(arr, getMissedElement(arr)))
    else:
        print('Text failed')
        break
else:
    print('Text successful')
