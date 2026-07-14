class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict()
        
        for num in nums:
            if num_dict.get(num):
                return True
            else:
                num_dict[num] = "x"
        
        return False