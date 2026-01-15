

def nonRep(s):
    size = 26
    appear = [-1] * size

    for i in range(len(s)):
        ind = ord(s[i]) - ord('a')
        if appear[ind] == -1:
            
            appear[ind] = i  
        else:
          appear[ind] = -2  

    idx = -1
    for i in range(size):
        if appear[i] >= 0 and (idx == -1 or appear[i] < appear[idx]):
            idx = i

    return '\$' if idx == -1 else s[appear[idx]]


s = "aabbccc"
print(nonRep(s))
