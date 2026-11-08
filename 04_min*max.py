class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def min_max_tree(arr):
    if len(arr) < 3:
        return -1
    i = 0
    while ((2*i + 1) < len(arr) ) and (arr[2*i + 1] != None):
        i = 2*i + 1
    mini = i
    i = 0
    while ((2*i + 2) < len(arr) ) and (arr[2*i + 2] != None):
        i = 2*i + 2
    maxi = i
    return arr[mini] *arr[maxi]

# В дереве поиска мин. и макс. элементы находятся в крайнем левом и кранйем правом узлах соответсвенно
# Поэтому для нахождения этих элементов нам нужно спуститься на глубину дерева => O(h)
