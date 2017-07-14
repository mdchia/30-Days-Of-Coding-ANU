def composeRanges(nums):
    if nums==[]:
        return []
    range_list=[]
    last_num=None
    curr_range=[]
    for num in nums:
        if last_num==None:
            curr_range=[num]
            last_num=num
            continue
        if num-last_num==1:
            curr_range+=[num]
            last_num=num
        else:
            if len(curr_range)==1:
                range_list+=[str(curr_range[0])]
            else:
                curr_str="{}->{}".format(curr_range[0],curr_range[-1])
                range_list+=[curr_str]
            curr_range=[num]
            last_num=num
    else:
        if not curr_range==[]:
            if len(curr_range)==1:
                range_list+=[str(curr_range[0])]
            else:
                curr_str="{}->{}".format(curr_range[0],curr_range[-1])
                range_list+=[curr_str]
    return range_list
