class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def min_height_tree(root):
    if root == None:
        return 0
    res = 1
    queue = [root]
    while len(queue) != 0:
        cnt_nodes = len(queue)
        for i in range(cnt_nodes):
            cur = queue.pop(0)
            if (cur.left == None) and (cur.right == None):
                return res
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)
        res += 1
    return res

# Использую BFS
# BFS эффективнее DFS, так как DFS проходит по всевозможным веткам дерева, 
# А BFS может дать ответ намного раньше 
