class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1 = 0 #best of the two previous houses
        rob2 = 0 #max of the previous and current value

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2