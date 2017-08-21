# -*- coding:utf-8 -*-
class Solution:
    # 请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
    def __init__(self):
        pass

    @staticmethod
    def replace_space(s):
        s = "%20".join(s.split(" "))
        return s


if __name__ == "__main__":
    test_target = "   dgdhdj kdkdj   dkdkjf   "
    solution = Solution()
    print solution.replace_space(test_target)
