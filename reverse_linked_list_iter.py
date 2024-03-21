class Node:
    def __init__(self, _val, _next):
        self._val = _val
        self._next = _next

ll = Node(1, Node(2, Node(3, Node(4,None))))

def print_ll(head):
    curr = head
    while curr:
        print(curr._val, end=" ")
        curr = curr._next

def reverse(head):
    prev = None
    curr = head
    _next = head
    while curr:
        _next = curr._next
        curr._next = prev
        prev = curr
        curr = _next
    return prev

print_ll(reverse(ll))