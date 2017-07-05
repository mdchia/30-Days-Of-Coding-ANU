def nextLarger(a):
    if a==[]:
        return []
    nums_seen=[]
    a.reverse()
    new_list=[]
    for i in a:
        larger_elements=[x for x in nums_seen if x>i]
        nums_seen.append(i)
        #print(larger_elements)
        if larger_elements==[]:
            new_list.append(-1)
        else:
            new_list.append(larger_elements[-1])
    new_list.reverse()
    return new_list
