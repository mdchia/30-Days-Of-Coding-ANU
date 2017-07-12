def initialChecks(s,x):
    if len(s)==1:
        if s==x:
            return 0
        else:
            return -1
    if len(x)>len(s):
        return -1
    return 1

# Implementation of Boyer–Moore–Horspool
def pp_dict(x):
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = {}
    for letter in alphabet:
        table[letter] = len(x)
    for i in range(len(x)-1):
        table[x[i]] = len(x)-1-i
    return table

def findFirstSubstringOccurrence(s, x):
    if not initialChecks(s,x)==1:
        return initialChecks(s,x)
    table = pp_dict(x)
    skip = 0
    x_l = len(x)
    s_l = len(s)
    while s_l - skip >= x_l:
        i = x_l-1
        while s[skip+i]==x[i]:
            if i==0:
                return skip
            i-=1
        skip = skip + table[s[skip + x_l-1]]
    return -1
