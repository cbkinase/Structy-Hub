def compress(s):
    i = 0
    j = 0
    result = []
    s += "!"
    
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            count = j - i
            
            if count == 1:
                result.append(s[i])
            else:
                result.append(f"{count}{s[i]}")
            i = j
    
    return "".join(result)
    