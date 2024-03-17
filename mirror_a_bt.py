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

def mirror_tree(root):
    if not root:
        return None
    if not root.left and not root.right:
        return root
    temp = root.left
    root.left = root.right
    root.right = temp
    mirror_tree(root.right)
    mirror_tree(root.left)
    return root

root = Node(10, Node(1, Node(6, None, None), None), Node(3, None, None))
print_tree(root)
print("mirrored")
print_tree(mirror_tree(root))
