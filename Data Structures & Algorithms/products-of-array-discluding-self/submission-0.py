class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1

                if zero_count > 1:
                    return [0] * len(nums)
                
                continue

            total_product *= num

        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(total_product)
                continue
            if zero_count > 0:
                output.append(0)
            else:
                output.append(total_product // nums[i])

        return output
