class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def sorted(arr):
            n = len(arr)
            for i in range(1, n):
                if arr[i-1] > arr[i]:
                    return False
            else:
                return True
        
        arr = nums[:] 
        answer = 0
        
        while not sorted(arr):
            cur_idx, cur_min_sum = 0, float('inf')
            for i in range(1, len(arr)):
                s = arr[i-1] + arr[i]
                if s < cur_min_sum:
                    cur_min_sum = s
                    cur_idx = i

            arr[cur_idx] = cur_min_sum
            del arr[cur_idx - 1]

            answer += 1
        
        return answer
            
