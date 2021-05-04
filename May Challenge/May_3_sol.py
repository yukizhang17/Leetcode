    def checkPossibility(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                res += 1
                if i>0 and i<len(nums) - 2 and nums[i-1]>nums[i+1] and nums[i]>nums[i+2]:
                    return False
        return res < 2
