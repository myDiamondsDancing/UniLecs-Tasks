def main(arr):
    negative = list()
    negative_sum = 0
    positive = list()
    positive_sum = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            negative_sum += (-1) * arr[i]
            negative.append(arr[i])
        elif arr[i] > 0:
            positive_sum += arr[i]
            positive.append(arr[i]) 

    if negative_sum > positive_sum:
        return negative
    else:
        return positive

def print_result(arr):
    string = '{'
    for el in arr:
        string += ' {},'.format(el)
    string += '}'    
    return string 

def test(dict_of_answers):
    i = 1
    for arr in dict_of_answers:
        if print_result(main(arr)) != dict_of_answers[arr]:
            return 'Test failed(test number {i})'.format(i)
        i += 1    

    return 'Test successful'  

print(test({ (-1, 1, 2, 3, -6) : '{ -1, -6,}', (-5, 6, 3, -1) : '{ 6, 3,}' }))   
