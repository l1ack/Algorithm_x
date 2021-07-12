class Node:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right
 
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
    # print(rear[-1]) 
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

 
def pre_order(t):
    if t == None:
        return
    print(t.data)
    pre_order(t.left)
    pre_order(t.right)
 
 
if __name__ == "__main__":
    rear = ['d','a','b','e','c']
    center = ['d','e','b','a','c']
    t = rebuild_rc(rear, center)
    pre_order(t)#t is already a tree.