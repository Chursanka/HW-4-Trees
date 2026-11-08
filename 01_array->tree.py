class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def arr_to_tree(arr, i):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = arr_to_tree(arr, 2*i + 1)
    root.right = arr_to_tree(arr, 2*i + 2)
    return root

# Данная функция находит в массиве корень исходного дерева. 
# Левый и правый потомки - тоже деревья (по определению дерева) => у левого и правого деревьев тоже есть корни => применяем данную функцию. 
# Так по математической индукции строится всё дерево
# Для хранения узлов дерева используется односвязный список, где каждый элемент может ссылаться не на один элемент, а на несколько
