# coding: utf-8


# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# 解题思路
# 使用队列，先将输入的 digits 中第一个数字对应的每一个字母入队，然后将出队的元素与第二个数字对应的每一个字母组合后入队...直到遍历到 digits 的结尾。最后队列中的元素就是所求结果

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[int(digit) - 2]:
                    queue.append(tmp + letter)
        return queue
