def getCountOfFor(haystack):
    count = 0
    i = -1
    while True:
        i = haystack.find('for', i+1)
        if i == -1:
            return count
        count += 1
        
def clipOnFor(string):
    lenght = len(string)
    count = 0
    count_of_back = 0
    count_of_frw = 0
    start = string.find('for')
    i = start + 3
    if start == -1:
        return 0
    while True:    
        if  string[i] == '{':
             count_of_frw += 1
        elif string[i] == '}':
             count_of_back += 1
        
        if count_of_back == count_of_frw:
             count += getCountOfFor(string[start : i+1]) 
             start = i
             count_of_back = 0
             count_of_frw = 0
             
        if i == len(string) - 1:
             break
             
        i += 1     
             
    return count

print(clipOnFor('for{for{for{for{}}}} for{for{for{}}}'))    
