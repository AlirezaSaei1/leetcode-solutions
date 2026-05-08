class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        max_val = max(nums)
        
        sieve = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if sieve[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if sieve[j] == j:
                        sieve[j] = i
        
        prime_to_indices = {}
        for idx, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = sieve[temp]
                if p not in prime_to_indices:
                    prime_to_indices[p] = []
                prime_to_indices[p].append(idx)
                while temp % p == 0:
                    temp //= p
        
        visited_indices = {0}
        visited_primes = set()
        queue = deque([(0, 0)])
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            if curr_idx == n - 1:
                return steps
            
            for next_idx in (curr_idx - 1, curr_idx + 1):
                if 0 <= next_idx < n and next_idx not in visited_indices:
                    visited_indices.add(next_idx)
                    queue.append((next_idx, steps + 1))
            
            val = nums[curr_idx]
            if val > 1 and sieve[val] == val:
                p = val
                if p in prime_to_indices and p not in visited_primes:
                    visited_primes.add(p)
                    for next_idx in prime_to_indices[p]:
                        if next_idx not in visited_indices:
                            visited_indices.add(next_idx)
                            queue.append((next_idx, steps + 1))
                    del prime_to_indices[p]
                    
        return -1