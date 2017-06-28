def merge_sort(arr1, swaps):
    if len(arr1)==1:
        return (arr1, swaps)
    breakpoint=(len(arr1)//2)
    a1=merge_sort(arr1[:breakpoint],swaps)
    a2=merge_sort(arr1[breakpoint:],swaps)
    swaps+=a1[1]+a2[1]
    l1=a1[0]
    l2=a2[0]
    arrf=[]
    x=0
    y=0
    while x!=len(l1):
        while y!=len(l2):
            if l1[x]<=l2[y]:
                arrf.append(l1[x])
                x+=1
            else:
                arrf.append(l2[y])
                y+=1
                swaps+=len(l1)-x
            if x==len(l1):
                arrf.extend(l2[y:])
                break
            #print (l2)
            #print (l1)
            #print (arrf)
        if y==len(l2):
            arrf.extend(l1[x:])
            break
    return (arrf, swaps)

def count_inversions(a):
    if a==None:
        return 0
    if len(a)==1:
        return 0
    sorted_list=merge_sort(a,0)
    return sorted_list[1]

def testy():
    print(count_inversions([1,1,1,2,2]))
    print(count_inversions([2,1,3,1,2]))

#t = int(input().strip())
#for a0 in range(t):
#    n = int(input().strip())
#    arr = list(map(int, input().strip().split(' ')))
#    print(count_inversions(arr))
