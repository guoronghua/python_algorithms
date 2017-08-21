# -*- coding:utf-8 -*-
# 输入一个链表，从尾到头打印链表每个节点的值。


class Node:
    def __init__(self, init_data):
        self.__data = init_data
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next


class SinCycLinkedList:
    # 单向循环链表
    def __init__(self):
        self.head = Node(None)
        self.head.set_next(self.head)

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head.get_next())
        self.head.set_next(temp)

    def remove(self, item):
        prev = self.head
        while prev.getNext() != self.head:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()

    def search(self, item):
        cur = self.head.get_next()
        while cur != self.head:
            if cur.getData() == item:
                return True
            cur = cur.get_next()

        return False

    def empty(self):
        return self.head.get_next() == self.head

    def size(self):
        count = 0
        cur = self.head.get_next()
        while cur != self.head:
            count += 1
            cur = cur.getNext()
        return count

    def re_print_list_val(self):
        list_val = []
        cur = self.head
        while cur:
            list_val.insert(0, cur.get_data())
            cur = cur.get_next()
        return list_val


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        pass

    @staticmethod
    def print_list_from_tail_to_head(list_node):
        list_val = []
        cur = list_node
        while cur:
            list_val.insert(0, cur.val)
            cur = cur.next
        return list_val
        # write code here


if __name__ == "__main__":
   pass
