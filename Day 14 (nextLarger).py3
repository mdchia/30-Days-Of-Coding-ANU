def nextLarger(a):
    def is_larger(x,i):
        return x>i
    if a==[]:
        return []
    nums_seen=[]
    a.reverse()
    l=a
    new_list=[]
    for i in l:
        larger_elements=[x for x in nums_seen if x>i]
        nums_seen.append(i)
        #print(larger_elements)
        if larger_elements==[]:
            new_list.append(-1)
        else:
            new_list.append(larger_elements[-1])
    new_list.reverse()
    return new_list
