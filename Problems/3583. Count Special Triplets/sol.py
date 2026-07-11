class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        freqPrev = Counter()
        freqNext = Counter(nums)
        
        ans = 0
        
        for x in nums:
            freqNext[x] -= 1
            if freqNext[x] == 0:
                del freqNext[x]
            
            target = 2 * x
            
            leftCount  = freqPrev.get(target, 0)
            rightCount = freqNext.get(target, 0)
            
            ans = (ans + leftCount * rightCount) % MOD
            
            freqPrev[x] += 1
        
        return ans
