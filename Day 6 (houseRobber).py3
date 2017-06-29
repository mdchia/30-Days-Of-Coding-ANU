def housePath(nums, curr_index, curr_val, max_val_at_index):
    curr_val+=nums[curr_index] # update current value
    if curr_index not in max_val_at_index:
        max_val_at_index[curr_index]=curr_val # initialise value
    else:
        if max_val_at_index[curr_index]<curr_val: # is this the maximum value we can get up to this index?
            max_val_at_index[curr_index]=curr_val # if it is, update the max
        else:
            return curr_val # if it's not, don't go down this path
    # To avoid consecutive numbers but maximise houses visited, either two or three houses ahead
    if curr_index+3 < len(nums):
        # print(curr_index) # debugging
        route1=housePath(nums, curr_index+2, curr_val, max_val_at_index)
        route2=housePath(nums, curr_index+3, curr_val, max_val_at_index)
        return max((route1,route2)) # which of those options gave us the most value?
    if curr_index+2 < len(nums):
        route1=housePath(nums, curr_index+2, curr_val, max_val_at_index)
        return route1 # if we're third last
    return curr_val # if we're last/second last
    # print(max_val_at_index) # debugging

def houseRobber(nums):
    max_val_at_index={}
    max_val=0
    nums_length=len(nums)
    if nums_length is 0:
        return 0
    if nums_length is 1:
        return nums[0]
    curr_val=0
    # start with the two possible first positions
    route1=housePath(nums, 0, curr_val, max_val_at_index)
    route2=housePath(nums, 1, curr_val, max_val_at_index)
    return max((route1,route2))
