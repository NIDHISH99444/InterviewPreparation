import sys
from collections import  defaultdict
from sys import  maxsize
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def kthSmallest(root):
    global k
    if not root :
        return
    left=kthSmallest(root.left)
    k-=1
    if k==0:
        return root.val

    right=kthSmallest(root.right)
    if left or right:
        return left or right


def distanceK( root, target, k):
    adj = defaultdict(list)
    def dfs(node):
        if node.left:
            adj[node.val].append(node.left.val)
            adj[node.left.val].append(node.val)
            dfs(node.left)
        if node.right:
            adj[node.val].append(node.right.val)
            adj[node.right.val].append(node.val)
            dfs(node.right)
    dfs(root)

    ans = []
    seen = set()

    def dfs2(root, k):
        if k == 0:
            ans.append(root)
        seen.add(root)
        for ele in adj[root]:
            if ele not in seen:
                dfs2(ele, k - 1)

    dfs2(target, k)
    print(seen)
    return ans


def goodNodes( root):

    map = {"count": 0}  #good way to use global count variable and increment

    def goodN(root, maxVal):
        if not root:
            return
        if root.val >= maxVal:
            map["count"] += 1
        maxVal = max(maxVal, root.val)
        goodN(root.left, maxVal)
        goodN(root.right, maxVal)

    maxVal = -sys.maxsize
    goodN(root, maxVal)
    return map["count"]

def check( root, subRoot):
    if not root and not subRoot:
        return True
    if (not root and subRoot) or (root and not subRoot):
        return False
    return root.val == subRoot.val and check(root.left, subRoot.left) and check(root.right, subRoot.right)

def isSubtree( root, subRoot):
    """
    :type root: TreeNode
    :type subRoot: TreeNode
    :rtype: bool
    """
    if not root and subRoot:
        return False
    if root.val == subRoot.val:
        return check(root, subRoot)
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def sortedArrayToBST( nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    def check(nums):

        if len(nums)==0:
            return
        mid = len(nums) // 2
        root = Node(nums[mid])
        root.left = check(nums[low:mid])
        root.right = check(nums[mid+1:high+1])
        return root

    return check(nums)


root=Node(3)
root.left=Node(4)
root.right=Node(5)
root.left.left=Node(1)
root.left.right=Node(2)

subRoot=Node(4)
subRoot.left=Node(1)
subRoot.right=Node(2)

print(sortedArrayToBST([1,2,3,4,5]))

# print(isSubtree(root,subRoot))

# root = Node(3)
# root.left = Node(5)
# root.right = Node(1)
# root.left.left = Node(6)
# root.left.right = Node(2)
# root.left.right.left=Node(7)
# root.left.right.right=Node(4)
# root.right.left=Node(0)
# root.right.right=Node(8)
# k=2
# print("kth smallest",kthSmallest(root))
#
# print(distanceK(root,5,2))
# count=0
# maxVal=-sys.maxsize
# print(goodNodes(root))
