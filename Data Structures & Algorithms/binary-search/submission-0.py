class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while(left <= right):
            curr = (right+left)//2
            mid = nums[curr]
            if(mid < target):
                left = curr +1
            elif(mid > target):
                right = curr -1
            else:
                return curr
        return -1;