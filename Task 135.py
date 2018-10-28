def get_summands(n):
    # Благодарю @jinxonik за предоставленный фрагмент кода из 130-ой задачи
    def generate(n, max_i, cur_list):
        max_i = min(n, max_i)
        yield cur_list + [1] * n

        for i in range(2, max_i + 1):
            if n - i == 0:
                yield cur_list + [i]
            else:
                yield from generate(n - i, i, cur_list + [i])

    if n <= 0: return None
    yield from generate(n, n, [])
    
def flag(arr):
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return False
    return True    
        
def main(n):
    listOfSummands = list(get_summands(n))  
    count = len(listOfSummands)
    for el in listOfSummands:
        if not flag(el):
            count -= 1
                        
    return count

for i in (3, 6, 8, 10, 15):
    print('{0} : {1}'.format(i, main(i))) 
