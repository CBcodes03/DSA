def find_duplicates(s):
    count = {}
    duplicates = {}
    
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char, cnt in count.items():
        if cnt > 1:
            duplicates[char] = cnt
    
    return duplicates
