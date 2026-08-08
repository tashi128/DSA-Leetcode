class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #created an empty dictionary to store nums

        for i, num in enumerate(nums): #loop through the list and get the key and values
            need = target - num 
            
            # need = 9 - 2 = 7 (1st iteration) wrong, so it moves to line 11, in 2nd iteration need = 9 - 7 = 2, which is inlcuded in seen, dictionary as key 2 : value 0 so it will return the seen[need], which is seen[2], which hold the value of 00 seen = { 2 : 0}, so it will return [0, 1], in place of seen[need], i, i reperesents the current index which was 1

            if need in seen:
                return [seen[need], i]

            seen[num] = i