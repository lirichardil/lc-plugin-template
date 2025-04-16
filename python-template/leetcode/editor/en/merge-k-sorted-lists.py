#
# @lc app=leetcode id=23 lang=python3
# @lcpr version=30104
#
# [23] Merge k Sorted Lists
#

from optparse import Option
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
    #解法1： 分治法、
    #第一步： 实现两个递增链表的合并
    def mergeTwoLists(self, list1:Optional[ListNode],list2:Optional[ListNode]):
        p1,p2 = list1,list2
        dummy = ListNode(-1)
        p = dummy
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else: 
                p.next = p1
                p1 = p1.next
            p = p.next
        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2
        return dummy.next
    def mergeKLists3(self, lists:List[Optional[ListNode]],start:int, end:int)-> Optional[ListNode]:
        if start == end:
            return lists[start]
        mid = start + (end - start) //2
        left = self.mergeKLists3(lists,start,mid)
        right = self.mergeKLists3(lists,mid+1,end)

        return self.mergeTwoLists(left,right)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeKLists3(lists,0,len(lists)-1)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

