class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Using Two Pointer Strategy
        left = 0 #left stores the index not the height
        right = len(height) - 1 #right stores index as well, and index starts at zero so if the height is 9 the index is 0 to 8 so right = 8
        best = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            best = max(best, area)

            if height[left] < height[right]:
                left += 1 #moves one number ahead left

            else:
                right -= 1 #right is going to move towards the left

        return best

