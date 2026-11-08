class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def cmp_trees(root1, root2):
    if (root1 == None) and (root2 == None):
        return True
    if (root1 == None) or (root2 == None):
        return False
    if root1.val != root2.val:
        return False
    return cmp_trees(root1.left, root2.left) and cmp_trees(root1.right, root2.right)

# Условия равенства:
# Одна и та же структура (оба пустые или оба непустые)
# Левые и правые поддеревья деревьев должны быть рекурсивоно равны 
# Равенство значений текущих узлов деревьев
