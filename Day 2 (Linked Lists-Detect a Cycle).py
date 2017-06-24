"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head == None:
        return False
    curr_node=head
    nodes_visited=set()
    while True:
        if curr_node.next == None:
            return False
        if curr_node in nodes_visited:
            return True
        else:
            nodes_visited.add(curr_node)
            curr_node=curr_node.next
