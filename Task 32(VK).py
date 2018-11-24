def main(string : str) -> str:
    returningString = ''
    for i in string:
        returningString += chr((ord(i) - 95) % 26 + 97)
        
    return returningString

print(main('this'))    
print(main('zoo'))
print(main('yam'))
