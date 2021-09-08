import  collections
class Node:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right
# type postorder: List[int] 
 # how to rebuild a tree.rear为后序,
#    *
#   / \
#  *   *
 # center为中序;
 #局部拆解，递归分解；都是从左子树开始，因为中序和后序左子树的索引相同
 #中序和先序的右子树索引相同！
def rebuild_rc(rear, center):
    if not rear:
        return
    cur = Node(rear[-1])
    print(rear[-1]) 
    print("----") 
    index = center.index(rear[-1])
    # print(index)
    cur.left = rebuild_rc(rear[:index], center[:index])
    # print("left")
    # print(rear[:index])
    # print(center[:index])
    # print("----")
    cur.right = rebuild_rc(rear[index:-1], center[index + 1:]) #rear[index:-1]是到倒数第二个数;
    # print("right")
    # print(rear[index:-1])
    # print(center[index + 1:])
    # print("----")
    return cur

def rebuild_pc(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild_pc(pre[1:index + 1], center[:index])
    cur.right = rebuild_pc(pre[index + 1:], center[index + 1:])
    return cur
 
def post_order(t):
    if t == None:
        return
    post_order(t.left)
    post_order(t.right)
    print(t.data)

def levelOrder(root: Node):
    if not root: return []
    res, deque = [], collections.deque([root])#层序遍历存储到队列
    while deque:
        tmp = collections.deque()
        for _ in range(len(deque)):#只值计算一次吗len(deque)
            node = deque.popleft()
            if len(res) % 2: tmp.appendleft(node.data) # 偶数层 -> 队列头部
            else: tmp.append(node.data) # 奇数层 -> 队列尾部
            if node.left: deque.append(node.left)
            if node.right: deque.append(node.right)
        res.append(list(tmp))
    print(res)

# 倒后序遍历,弹栈
# def verifyPostorder(self, postorder):
#     stack, root = [], float("+inf")
#     for i in range(len(postorder) - 1, -1, -1):
#         # print(stack)
#         # print(root)
#         if postorder[i] > root: return False
#         while(stack and postorder[i] < stack[-1]):
#         #现在的数小于栈尾，弹栈，直到栈尾小于当前数;也就是第一个大于当前数的数作为root，
#         #stack[-1]表示栈尾，也是倒后序遍历最新读到的数字;
#         #这里表示数字开始递减，表明开始遇到左子树，root
#         #对于原数组，最后一个一定是root,但是对于接下来，如何判断root，
#         #右子树入栈是为了判断根节点root，
#             root = stack.pop()
#         stack.append(postorder[i])
#         print(root)
#     return True
        # """
        # :type postorder: List[int]
        # :rtype: bool
        # """

def pre_order(t):
    if t == None:
        return
    print(t.data)
    pre_order(t.left)
    pre_order(t.right)

def center_order(t):
    if t == None:
        return
    pre_order(t.left)
    print(t.data)
    pre_order(t.right) 

 #从树反推生成序列
def BSTSequences(root: Node):
    if not root: return [[]]
    ans_all=[]
    def dfs(root, que, path):#que[0:i]未排序节点(即右子树的根节点)que[i+1:](此节点的左右子树)
        if root.left: 
            que.append(root.left)
        if root.right: 
            que.append(root.right)
        if not que: 
            ans_all.append(path)
            # print(path)
            #如果没有待排序子树que,那么将完整的path存进结果中,为什么que不大于2,que指向相邻子树根节点或者子节点
        # print(len(que))
        for i in range(len(que)):#回溯法将子序列一一排序,直到用完
            dfs(que[i], que[0:i]+que[i+1:], path+[que[i].data])
    dfs(root, [], [root.data])
    return ans_all

#enumerate枚举
def pathSum(self, root: Node, sum: int) -> int:
    dp = {}

    def search(root: Node):
        if root:
            search(root.left)
            search(root.right)
            dp[root] = [root.val] # 1
        
            if root.left: # 2
                for i, t in enumerate(dp[root.left]):
                    dp[root].append(t + root.val)#t即所有枚举出来的值t,加入到doop[root]中
                
            if root.right: # 3
                for i, t in enumerate(dp[root.right]):
                    dp[root].append(t + root.val)
                
    search(root)
    res = 0
    for (_, v) in dp.items():#包含dp枚举的集合
        for t in v:
            if t == sum:
                res += 1
    return res

# #如何建树，先序遍历
# def build_tree(root:Node,list:List<int>):
#     root.data=list[0]
#     for i in range(list):
#         if (list[i]<root):root.left=list[i]
#         else:root.right=list[i]
#     if 

#先序遍历建树
def build_tree(arrs):
    if len(arrs)!=0:
        if(arrs[0]==None):
            arrs.pop(0)
            return None
        tree=Node(arrs[0])#首节点为node类型的首节点arrs0
        arrs.pop(0)#arrs去掉首节点，先建左树再建右树！
        tree.left=build_tree(arrs)
        tree.right=build_tree(arrs)
        return tree
    else:
        return None

#层序遍历建树
def create_BTree_By_List(array):
    i = 1
    # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
    level_order = []
    sum = 1

    while sum < len(array):
        level_order.append(array[i-1:2*i-1])
        i *= 2
        sum += i
    level_order.append(array[i-1:])
    # print(level_order)

    # BTree_list: 这一层所有的节点组成的列表
    # forword_level: 上一层节点的数据组成的列表
    def Create_BTree_One_Step_Up(BTree_list, forword_level):

        new_BTree_list = []
        i = 0
        for elem in forword_level:
            root = Node(elem)
            if 2*i < len(BTree_list):
                root.left = BTree_list[2*i]
            if 2*i+1 < len(BTree_list):
                root.right = BTree_list[2*i+1]
            new_BTree_list.append(root)
            i += 1

        return new_BTree_list

    # 如果只有一个节点
    if len(level_order) == 1:
        return Node(level_order[0][0])
    else: # 二叉树的层数大于1

        # 创建最后一层的节点列表
        BTree_list = [Node(elem) for elem in level_order[-1]]

        # 从下往上，逐层创建二叉树
        for i in range(len(level_order)-2, -1, -1):
            BTree_list = Create_BTree_One_Step_Up(BTree_list, level_order[i])

        return BTree_list[0]

# #中序遍历建树不太可能
# def build_tree_center(arrs):
#     if len(arrs)!=0:
#         if(arrs[0]==None):
#             arrs.pop(0)
#             return None
#         tree=Node([])#首节点为node类型的首节点arrs0
#         tree.left=Node(arr[0])
#         arrs.pop(0)#arrs去掉首节点，先建左树再建右树！
#         tree.data=build_tree(arrs)
#         tree.right=build_tree(arrs)
#         return tree
#     else:
#         return None

if __name__ == "__main__":
    pre = ['d','a','c','e','b','g','f']
    center = ['a','b','c','d','e','f','g']
    # pre = [1,6,7,3,0,2,8]
    # center = ['a','b','c','d','e','f','g']
    # t = rebuild_pc(pre, center)
    # post_order(t)#t is already a tree.
    # BSTSequences(t)
    # print('*******')
    #print(BSTSequences(t))
    t=build_tree(pre)
    # print(pre_order(t))
    # print(center_order(t))
    print(levelOrder(t))
