def main(arr : list) -> list:
     #Идея проста: создаем массив такой же длины, что и массив на входе
     #А затем просто в начало добавляем ненулевые элементы
     
     i = 0
     
     for j in range(len(arr)):
        if arr[j] != 0 :
            arr[i] = arr[j]
            i += 1
            
     for k in range(i, len(arr)):
        arr[k] = 0     

     return arr

print(main([0, 4, 5, -1, 9, 9, 0, 54]))    
