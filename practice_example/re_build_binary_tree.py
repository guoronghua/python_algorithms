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


