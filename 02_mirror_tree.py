class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_mirror(left, right):
        if (left == None) and (right == None):
            return True
        if (left == None) and (right == None):
            return False
        if (left.val != right.val):
            return False
        return (is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
                
def mirror_tree(root):
    if root == None:
        return True
    return is_mirror(root.left, root.right)


# Работа рекурсивной функции: 
# Прохожу дерево BFD
# сравниваю значения узлов слева и справа (а также структуру - пусто или нет), а потом сравниваю у каждого из них левые и правые узлы
