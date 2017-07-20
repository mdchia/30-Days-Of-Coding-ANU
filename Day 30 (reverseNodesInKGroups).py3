# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def reverseNodesInKGroups(l, k):
    if k==1 or l.next==None:
        return l
    if l==None:
        return None
    def countNodes(l):
        if l==None:
            return 0
        i=0
        curr=l
        while curr!=None:
            i+=1
            curr=curr.next
        return i
    def printNodes(l):
        curr=l
        while curr!=None:
            print(str(curr.value)+",", end='')
            curr=curr.next
        print()
    #print('start')
    i=0
    last_head=None
    curr=l
    nexty=None
    while curr!=None:
        prev=None
        curr_head=curr
        i=0
        #printNodes(curr)
        if countNodes(curr)<k:
            last_head.next=curr
            break
        while curr!=None and i<k: # reshuffle pointers
            nexty=curr.next
            curr.next=prev
            prev=curr
            curr=nexty
            i+=1
            #print(i)
        if last_head is not None:
            last_head.next=prev
        else:
            o=prev # this'll be the head of the first reversed list
        last_head = curr_head
    #print('end')
    return o # final head
