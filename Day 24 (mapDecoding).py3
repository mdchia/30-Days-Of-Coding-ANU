
def mapDecoding(message):
    char_min = 1
    char_max = 26
    max_head_len = 2
    checked_options = [0]*(len(message)+1)
    checked_options[len(message)]=1
    for x in range(len(message), -1, -1): #going backwards through string
        hs=1
        while True:
            if hs > max_head_len:
                break
            if hs+x > len(message):
                break
            head = message[x:x+hs]
            #print("x:{}, hs:{}, head:{}".format(x,hs,head))
            if not char_min <= int(head) <= char_max:
                break
            checked_options[x]+=checked_options[x+hs]
            hs+=1
        #print(checked_options)
    return checked_options[0]%(10**9+7)
