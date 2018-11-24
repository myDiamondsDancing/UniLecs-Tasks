def main(string : str) -> str:
    return ''.join([chr((ord(i) - 95) % 26 + 97) for i in string])

print(main('this'))    
print(main('zoo'))
print(main('yam'))
