class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root: Node):
    if not root:
        return
    print(root.val, end=", ")
    print_tree(root.left)
    print_tree(root.right)

def next_greater(pre_order: list):
    root = pre_order[0]
    idx = 1
    while idx < len(pre_order):
        if root < pre_order[idx]:
            return idx
        idx += 1
    return -1
        
def construct_bst(pre_order: list) -> Node:
    if not pre_order:
        return None
    if len(pre_order) == 1:
        return Node(pre_order[0], None, None)
    root = Node(pre_order[0], None, None)
    _next_greater = next_greater(pre_order)
    start_left = 1
    end_left = _next_greater - 1
    start_right = _next_greater
    root.left = construct_bst(pre_order[start_left:end_left+1])
    root.right = construct_bst(pre_order[start_right:])
    return root

print_tree(construct_bst([10, 5, 1, 7, 40, 50]))
     