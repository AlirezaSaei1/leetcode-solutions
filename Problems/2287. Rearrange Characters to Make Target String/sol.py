class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count = Counter(s)
        target_count = Counter(target)
        
        answer = float('inf')
        for char, required_freq in target_count.items():
            possible_copies = s_count[char] // required_freq
            answer = min(answer, possible_copies)
            
        return answer