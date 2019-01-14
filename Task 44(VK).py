def main(e : str, arr : list) -> list:
    for i in range(len(arr) - 4):
        if arr[i : i+5] == [e] * 5:
            return True
            
    return False
