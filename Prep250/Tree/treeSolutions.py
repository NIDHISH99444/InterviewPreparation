class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def rightSideView(root):
    if not root :
        return
    queue=[root]
    ll=[]

    while queue:
        flag=0
        for i in range(len(queue)):
            node=queue.pop(0)
            if flag==0:
                flag=1
                res.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    return res

def leftLeaf(root):
    if not root:
        return
    queue = [root]
    ll = []
    sum=0
    while queue:

        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                ele=node.left
                if not ele.left and not ele.right:
                    sum+=ele.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return sum

res=[]
def treePath(root,path):
    if not root:
        return
    path += str(root.val) + "->"
    if not root.left and not root.right:
        res.append(path[:-2])
        return

    treePath(root.left, path)
    treePath(root.right, path)

maxCount=0
def maxDepth(root,cnt):
    if not root :
        return cnt
    cnt+=1
    leftC=maxDepth(root.left,cnt)
    rightC=maxDepth(root.right,cnt)
    return max(leftC,rightC)

def isSymmetric(root):
    if not root:
        return True
    root1=root.left
    root2=root.right
    def checkSym(root1,root2):
        if (not root1 and root2 )  or (not root2 and root1):
            return False
        if not root1 and not root2:
            return  True
        return root1.val==root2.val and checkSym(root1.left,root2.right) and checkSym(root1.right,root2.left)
    return (checkSym(root1,root2))

maxCount=0
def isBalanced(root,cnt):
    if not root :
        return cnt
    cnt+=1
    leftC=isBalanced(root.left,cnt)
    rightC=isBalanced(root.right,cnt)
    if leftC and rightC and abs(leftC-rightC)<=1:
        return max(leftC,rightC)
    else:
        return False

def zigZagTraversal(root):
    if not root:
        return []
    s1,s2=[],[]
    s1.append(root)
    ll=[]

    while s1 or s2 :
        res=[]
        while s1:
            ele=s1.pop()
            res.append(ele.val)
            if ele.left:
                s2.append(ele.left)
            if ele.right:
                s2.append(ele.right)

        ll.append(res)
        res=[]
        while s2 :
            ele=s2.pop()
            res.append(ele.val)
            if ele.right:
                s1.append(ele.right)
            if ele.left:
                s1.append(ele.left)

        ll.append(res)
    print("ll",ll)
    if not ll[-1]:
        return ll[:-1]
    return ll


def lowestCommonAncestor( root, p, q):
    if not root:
        return
    if root.val==p or root.val==q :
        return root.val
    left=lowestCommonAncestor(root.left,p,q)
    right=lowestCommonAncestor(root.right,p,q)
    if left and right:
        return root.val
    if left:
        return left
    else:
        return right


def validateBinarySearchTree(root, l=float('-inf'), r=float('inf')):
    if not root :
        return True
    if root.val <= l or root.val >=r:
        return False

    return validateBinarySearchTree(root.left,l,root.val) and validateBinarySearchTree(root.right,root.val,r)
val=[]


def kthSmallest(root):
    global k
    if not root :
        return
    left=kthSmallest(root.left)
    k-=1
    if k==0:
        return  root.val
    right=kthSmallest(root.right)
    if left or right:
        return left or right






# root = Node(2)
# root.left = Node(1)
# root.right = Node(3)
# root.left.left = Node(6)
# root.left.right = Node(2)
# root.right.left= Node(0)
# root.right.right= Node(8)
# root.left.right.left=Node(7)
# root.left.right.right=Node(4)
# root.right.right = Node(3)
# res = isBalanced(root, 0)

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
# root.right.left= Node(0)
# root.right.right= Node(8)
root.left.left.left=Node(1)
k=5
print(kthSmallest(root))
# print(val[k-1])
# root.left.right.right=Node(4)
# root.right.right = Node(3)

# print(validateBinarySearchTree(root))

# isBalanced(root,0)
# path=""
# treePath(root,path)
# print(res)
# print(zigZagTraversal(root))

# print(rightSideView(root))

# print(lowestCommonAncestor( root, 5, 1))
# print(maxDepth(root,0))
# print(isSymmetric(root))
# print(levelOrderTraversal(root))
# print(leftLeaf(root))