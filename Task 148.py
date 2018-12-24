def main(arr : list) -> list:
     #Идея проста: создаем массив такой же длины, что и массив на входе
     #А затем просто в начало добавляем ненулевые элементы
     
     arr2 = [0] * len(arr)
     i = 0
     
     for j in range(len(arr)):
        if arr[j] != 0 :
            arr2[i] = arr[j]
            i += 1

     return arr2

print(main([0, 4, 5, -1, 9, 9, 0, 54]))    
