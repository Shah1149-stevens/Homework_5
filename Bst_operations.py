# bst.py
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def add(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = add(root.left, val)
    elif val > root.val:
        root.right = add(root.right, val)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=", ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.val, end=", ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, val):
    if root is None:
        return root

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete(root.right, min_node.val)

    return root

def main():
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))

    root = None
    for val in arr:
        root = add(root, val)

    print("in-order traversal: ", end="")
    inorder_traversal(root)
    print()

    delete_val = int(input("input a value to delete: "))
    new_root = delete(root, delete_val)

    print("pre-order traversal after deletion", end="")
    if delete_val not in arr:
        print(" ({} doesn't exist): ".format(delete_val), end="")
    else:
        print(" ({} is deleted): ".format(delete_val), end="")

    preorder_traversal(new_root)
    print()

if __name__ == "__main__":
    main()