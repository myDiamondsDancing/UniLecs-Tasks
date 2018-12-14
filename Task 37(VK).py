def main(arr):
    sum_of_negative = 0
    sum_of_positive = 0
    negative = list()
    positive = list()
    for i in arr:
        if i < 0:
            sum_of_negative += i
            negative.append(i)
        elif i > 0:
            sum_of_positive += i
            positive.append(i)
            
    if sum_of_negative * (-1) > sum_of_positive:
           return negative
            
    return positive

print(main([1, 2, 3, -1, -54, 5]))  
