#
# @lc app=leetcode id=264 lang=python3
# @lcpr version=30201
#
# [264] Ugly Number II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2,p3,p5 = 1,1,1
        product2,product3,product5 = 1,1,1
        ugly = [0] * (n+1)

        p = 1

        while p <= n:
            min_val = min(product2,product3,product5)
            ugly[p] = min_val
            p += 1
            #判断重复的情况
            if min_val == product2:
                product2 = 2* ugly[p2]
                p2 += 1
            if min_val == product3:
                product3 = 3*ugly[p3]
                p3 += 1
            if min_val == product5:
                product5 = 5*ugly[p5]
                p5 += 1
        
        return ugly[n]


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

