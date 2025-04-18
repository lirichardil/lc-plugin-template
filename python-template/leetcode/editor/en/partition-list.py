#
# @lc app=leetcode id=86 lang=python3
# @lcpr version=30104
#
# [86] Partition List
#

import sys
import os

from networkx import null_graph

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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1,p2 = dummy1,dummy2
        
        # p 负责遍历原链表，类似合并两个有序链表的逻辑
        # 这里是将一个链表分解成两个链表
        p = head
        while p: 
            if p.val >= x:
                p2.next = p
                p2 = p2.next
                
            else:
                p1.next = p
                p1 = p1.next
            # 不能直接让 p 指针前进，
            # p = p.next
            # 断开原链表中的每个节点的 next 指针
            temp = p.next
            p.next = None
            p = temp

        #链接两个链表：
        p1.next = dummy2.next #p2已经为dummy2后面添加了元素了，p2的开头就是dummy2

        return dummy1.next #直接返回dummy1就可以了

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    L = ListNode.create_head([1,4,5,22,34,7])
    res = solution.partition(L,7)
    ListNode.print(res)
#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

