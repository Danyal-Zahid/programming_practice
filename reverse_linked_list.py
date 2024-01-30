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

def reverse(head, new_head=None):
    if head is None:
        return None, None
    reversed, new_head = reverse(head._next)
    if reversed:
        reversed._next = head
        head._next = None
    else:
        new_head = head
    return head, new_head

_, new_head = reverse(ll)
print_ll(new_head)


