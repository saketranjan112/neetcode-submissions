class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
                continue
            freq[i] = 1

        buckets = [[] for n in range(len(nums) + 1)]

        for n, c in freq.items():
            buckets[c].append(n)

        res = []
        reslen = 0

        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                res.append(num)
                reslen += 1
                if reslen == k:
                    return res