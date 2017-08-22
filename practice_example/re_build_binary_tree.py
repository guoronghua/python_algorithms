# -*- coding:utf-8 -*-


class BinaryTree(object):
    # 二叉树的类实现
    def __init__(self, item):
        self.key = item
        self.left_child = None
        self.right_child = None

    def insert_left(self, item):
        if not self.left_child:
            self.left_child = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, item):
        if not self.right_child:
            self.right_child = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.right_child = self.right_child
            self.right_child = t


# 先序遍历(pr_eorder travelsal)
# 先打印出根，然后递归的打印出左子树、右子树，对应先缀表达式
def pre_order(tree, nodelist=None):
    if nodelist is None:
        nodelist = []
    if tree:
        nodelist.append(tree.key)
        pre_order(tree.left_child, nodelist)
        pre_order(tree.right_child, nodelist)
    print nodelist


# 中序遍历(in_order travelsal)
# 先递归的打印左子树，然后打印根，最后递归的打印右子树，对应中缀表达式
def in_order(tree):
    if tree:
        in_order(tree.left_child)
        print tree.key
        in_order(tree.right_child)


# 后序遍历(re_order travelsal)
# 递归的打印出左子树、右子树，然后打印根，对应后缀表达式
def re_order(tree):
    if tree:
        for key in re_order(tree.left_child):
            yield key
        for key in re_order(tree.right_child):
            yield key
        yield tree.key


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    # 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列
    # {1, 2, 4, 7, 3, 5, 6, 8}
    # 和中序遍历序列
    # {4, 7, 2, 1, 5, 3, 8, 6}，则重建二叉树并返回。

    def re_construct_binary_tree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            # 创建根节点，根节点肯定是前序遍历的第一个数
            root = TreeNode(pre[0])
            # 找到中序遍历根节点所在位置, root_index中
            root_index = tin.index(pre[0])

            # 对于中序遍历，根节点左边的节点位于二叉树的左边，根节点右边的节点位于二叉树的右边

            left_pre = pre[1:root_index + 1]
            left_in = tin[:root_index]
            root.left = self.re_construct_binary_tree(left_pre, left_in)

            right_pre = pre[root_index + 1:]
            right_in = tin[root_index + 1:]
            root.right = self.re_construct_binary_tree(right_pre, right_in)
        return root
        # write code here

if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    solution = Solution()
    solution.re_construct_binary_tree(pre, tin)
