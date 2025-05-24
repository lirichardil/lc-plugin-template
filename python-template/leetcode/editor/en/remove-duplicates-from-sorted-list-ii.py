#
# @lc app=leetcode id=82 lang=python3
# @lcpr version=30201
#
# [82] Remove Duplicates from Sorted List II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p, q = dummy, head
        while q is not None:
            if q.next is not None and q.val == q.next.val:
                # 发现重复节点，跳过这些重复节点
                while q.next is not None and q.val == q.next.val:
                    q = q.next
                q = q.next
                # 此时 q 跳过了这一段重复元素
                if q is None:
                    p.next = None
                # 不过下一段元素也可能重复，等下一轮 while 循环判断
            else:
                # 不是重复节点，接到 dummy 后面
                p.next = q
                p = p.next
                q = q.next
        return dummy.next
    
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

