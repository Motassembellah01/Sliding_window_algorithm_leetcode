import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Compare current max to new num in window -> when we created the window of size k 
        # Remove the max value calculated in previous window and consider second maximum value
        # Create deque where we store numbers in monotically decreasing order

        q = collections.deque()
        result = []

        l, r = 0, 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r - l + 1) == k:
                result.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return result







