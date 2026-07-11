class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        NEG = -10**30
        
        s0 = nums[0]
        s1 = s2 = s3 = NEG
        ans = NEG
        
        for i in range(1, len(nums)):
            x = nums[i]
            if nums[i] > nums[i - 1]:
                ns0 = x
                ns1 = max(s1 + x, s0 + x)
                ns2 = NEG
                ns3 = max(s3 + x, s2 + x)
            elif nums[i] < nums[i - 1]:
                ns0 = x
                ns1 = NEG
                ns2 = max(s2 + x, s1 + x)
                ns3 = NEG
            else:
                ns0 = x
                ns1 = ns2 = ns3 = NEG
            
            s0, s1, s2, s3 = ns0, ns1, ns2, ns3
            if s3 > ans:
                ans = s3
        
        return ans
