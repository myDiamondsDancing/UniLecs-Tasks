def main1(N, M, point):
    count = ( N * (point[0] - 1) + point[1] if point[0] % 2 == 1 
                    else N * (point[0] - 1) + N - point[1] + 1) 
    return count

def main2(N, M, point):
    count = 0
    for i in range(point[0]):
        if i == point[0] - 1:
            if i % 2 == 0:
                count += point[1]
            else:
                count += N - point[1] + 1
        else:
            count += N  
    return count    

def testing(func1, func2, data):
    for arg in data:
        if func1(*arg) != data[arg] or func2(*arg) != data[arg]:
            print('Test failed')
            return
        else:
            print('Data : {}, answer : {}'.format(arg, func1(*arg)))    
    print('Test complited')         

# If you want to check another variants, add this to data
# Data - hashmap<data, answer>
data = {
    (10, 8, (4, 7)) : 34,
    (10, 8, (7, 4)) : 64,
    (3, 3, (2, 1)) : 6
}

testing(main1, main2, data)
