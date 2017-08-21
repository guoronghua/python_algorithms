# -*- coding:utf-8 -*-
class Solution:
    # 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    # 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    def __init__(self):
        pass

    @staticmethod
    def find(target, array):
        row_count = len(array)
        col_count = len(array[0])
        x = row_count - 1
        y = 0
        while x >= 0 and y < col_count:
            if array[x][y] == target:
                return True
            if array[x][y] > target:
                x -= 1
                continue
            if array[x][y] < target:
                y += 1
                continue
        return False


if __name__ == "__main__":
    test_target = 7
    test_array = [[1, 2, 8, 9],
                  [2, 4, 9, 12],
                  [4, 7, 10, 13],
                  [6, 8, 11, 15]
                  ]
    solution = Solution()
    print solution.find(test_target, test_array)
