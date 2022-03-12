class Node(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data
        
def Level_sum(root,arr,n,level):
    if root is None:
        return
    if (root != None):
        #Recursively calling left-subtree while incrementing the level:
        Level_sum(root.left,arr,n,(level + 1)) 
        #adding all nodes values belonging to same level
        arr[level] += root.val
        #Recursively calling right-subtree while incrementing the level
        Level_sum(root.right,arr,n,(level + 1)) 
        
def Height(root):
    
    #Finding the height of the tree:
    #Height of tree = Max(Height(leftsubtree,rightsubtree) + 1)
    if root is None:
        return 0
    lheight = Height(root.left)
    rheight = Height(root.right)
    return(max(lheight,rheight) + 1)

def Insert(root):
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right.left = Node(13)
    return(root)

def main():
    root = None
    root = Insert(root)
    h = Height(root)
    arr = [0]*h
    n_elements = [0]*h
    Level_sum(root,arr,n_elements,0)
    count = 0
    for i in arr:
        print('sum of all nodes at',count,'level is:',i)
        count += 1
    print('Maximum sum is:',max(arr))

if __name__ == "__main__":
    main()


