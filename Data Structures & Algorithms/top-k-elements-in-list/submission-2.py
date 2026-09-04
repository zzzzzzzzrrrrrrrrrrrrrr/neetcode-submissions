class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        counter_key = list(counter.keys())

        result = sorted(counter_key, key=counter.__getitem__, reverse=True)
    
        return result[0: k]

