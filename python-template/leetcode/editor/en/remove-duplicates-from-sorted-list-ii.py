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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyUniq = ListNode(101)
        dummyDup = ListNode(101)

        pUniq,pDup = dummyUniq,dummyDup
        p = head

        while p:
            if(p.next is not None and p.val == p.next.val) or p.val == pDup.val:
                pDup.next = p 
                pDup = pDup.next
            else:
                pUniq.next = p
                pUniq = pUniq.next
            
            p = p.next

            #将新建的链表和原链表断开。 因为pUniq.next = p 这一步， p后面还跟了原列表后面的东西
            pUniq.next = None
            pDup.next = None 
            #最终返回dummyUniq这个头节点跟的链表。
        return dummyUniq.next
        

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

