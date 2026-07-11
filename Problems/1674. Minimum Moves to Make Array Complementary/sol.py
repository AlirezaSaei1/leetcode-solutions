class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # Range for 0 moves
            target_0 = a + b
            
            # Range for 1 move
            min_1 = min(a, b) + 1
            max_1 = max(a, b) + limit
            
            # Apply cost adjustments using difference array
            # 2 moves everywhere by default for this pair
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # Reduce cost to 1 move within [min_1, max_1]
            diff[min_1] -= 1
            diff[max_1 + 1] += 1
            
            # Reduce cost to 0 moves at exactly target_0
            diff[target_0] -= 1
            diff[target_0 + 1] += 1
            
        ans = n  # Maximum possible moves is changing all n elements
        current_moves = 0
        
        for target_sum in range(2, 2 * limit + 1):
            current_moves += diff[target_sum]
            if current_moves < ans:
                ans = current_moves
                
        return ans