class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_palindrome(arr): # функция взята из ДЗ 2, задача 6
    le = 0
    ri = len(arr) - 1
    while (le < ri):
        if arr[le] != arr[ri]:
            break
        else:
            le += 1
            ri -= 1
    return le >= ri

def add_subtree(arr, root):
    if root != None:
        add_subtree(arr, root.left)
        arr.append(root.val)
        add_subtree(arr, root.right)

def mirror_tree(root):
    if root == None:
        return True
    array_of_nodes = []
    add_subtree(array_of_nodes, root)
    return is_palindrome(array_of_nodes)

# Работа рекурсивной функции: 
# Cоздаю список узлов в виде LNR
# если получившийся массив - палиндром, то дерево - симметричное
