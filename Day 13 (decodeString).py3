def multiplyString(s, n):
    final_string=""
    within_brackets=False
    substring=""
    levels=0
    next_n=""
    for l in s:
        if l.isdigit():
            if not within_brackets:
                next_n+=l
            else:
                substring+=l
        elif l=="[":
            levels+=1
            if levels>1:
                substring+=l
            if not within_brackets:
                within_brackets=True
                next_n=int(next_n)
        elif l=="]":
            levels-=1
            #print(levels)
            #print(substring)
            #print(final_string)
            if levels==0:
                final_string+=multiplyString(substring, next_n)
                substring=""
                within_brackets=False
                next_n=""
            else:
                substring+=l
        elif within_brackets:
            substring+=l
        else:
            final_string+=l
    final_string=final_string*n
    return final_string

def decodeString(s):
    return multiplyString(s,1)
