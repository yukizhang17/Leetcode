    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        else:
            counter = 0
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    counter += 1
                    if i > 0 and i < n-2:
                        if nums[i-1] > nums[i+1] and nums[i] > nums[i+2]:
                            return False
                if counter >= 2:
                    return False
            return True
