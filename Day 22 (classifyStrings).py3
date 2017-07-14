def classifyString(s):
    cons_in_row=0
    vowl_in_row=0
    vowels=["a", "e", "i", "o", "u"]
    last_char='' # can be v or c
    for l in s:
        if last_char=='':
            if l in vowels:
                vowl_in_row=1
                last_char='v'
                continue
            else:
                cons_in_row=1
                last_char='c'
                continue
        if l in vowels:
            if last_char=='v':
                vowl_in_row+=1
            if last_char=='c':
                vowl_in_row=1
                last_char='v'
        else:
            if last_char=='c':
                cons_in_row+=1
            if last_char=='v':
                cons_in_row=1
                last_char='c'
        if vowl_in_row==3 or cons_in_row==5:
            return "bad"
        #print(vowl_in_row)
        #print(cons_in_row)
    return "good"

def consecutiveQs(s):
    qs_in_row=0
    last_char=''
    qs={'maximum':0,'total':0}
    for l in s:
        if l == '?':
            qs['total']+=1
            if last_char=='?':
                qs_in_row+=1
            else:
                qs_in_row=1
            if qs_in_row>qs['maximum']:
                qs['maximum']=qs_in_row
    return qs

import itertools

def classifyStrings(s):
    if len(s)<3:
        return "good"
    if not '?' in s:
        return classifyString(s)
    q_test=consecutiveQs(s)
    if q_test['maximum']>4:
        return "mixed"
    splitted=s.split('?')
    combos=itertools.product('ac', repeat=q_test['total'])
    last_str=''
    for combo in combos:
        combo=list(combo)+['']
        curr_str=splitted+combo
        curr_str[::2]=splitted
        curr_str[1::2]=combo
        curr_str=''.join(curr_str)
        #print(curr_str)
        testy=classifyString(curr_str)
        #print(testy)
        if last_str=='':
            last_str=testy
        if not last_str==testy:
            return 'mixed'
    return last_str
