from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        right = 0
        output = [] #gonna contain the maximum element of every sliding window

        q = deque() # will contain the values being added to the queue and will contain the values always in decreasing format, if the new value is greater than the current right most value we'll pop it from the queue, else we'll add it to the window and then return the maximum value from each sliding window and add it to the queue

        while right < len(nums): #while right is in bounds
            while q and nums[q[-1]] < nums[right]: #while q is non empty and the rightmost element in the queue is less than the current right means the new value that we added in the window, pop that value
                q.pop()

            #if the new value in the window is less than the right most value in the queue then just simply add it in the queue
            q.append(right)

            #remove the left value from the window
            if q[0] < left:
                q.popleft()

            if (right + 1) >= k:

                output.append(nums[q[0]])
                left += 1
            
            right += 1

        return output




            





        