# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    if l==None:
        return True
    if l.next==None:
        return True
    def reverseList(l_n):
        prev=None
        curr=l_n
        nexty=None
        while curr!=None: # reshuffle pointers
            nexty=curr.next
            curr.next=prev
            prev=curr
            curr=nexty
        return prev # this'll be the head of the reversed list
    def isEqualLists(l1,l2):
        curr1=l1
        curr2=l2
        while curr1!=None:
            if curr2==None:
                return False
            if curr1.value!=curr2.value:
                return False
            curr1=curr1.next
            curr2=curr2.next
        return True
    rabbit=l # fast pointer
    tortoise=l # slow pointer
    while (rabbit!=None and rabbit.next!=None):
        last_tortoise=tortoise
        rabbit=rabbit.next.next
        tortoise=tortoise.next
    if rabbit!=None: # if there's odd list length
        tortoise=tortoise.next # then push the slow pointer past the middle node
    last_tortoise.next=None # break the original list in the middle
    return isEqualLists(l,reverseList(tortoise))
