# -*- coding:utf-8 -*-
class Solution:
    # 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组
    # {3, 4, 5, 1, 2}
    # 为
    # {1, 2, 3, 4, 5}
    # 的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        first = rotateArray[0]
        while 1:
            length = len(rotateArray)
            if length == 1:
                return first
            mid = rotateArray[int(length / 2)]
            if mid > first:
                rotateArray = rotateArray[int(length / 2):length]
            if mid < first:
                index = int(length / 2)
                while index > 0:
                    index = index - 1
                    if rotateArray[index] > first:
                        return rotateArray[index + 1]
