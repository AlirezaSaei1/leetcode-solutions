class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved[row].add(seat)
        
        answer = 2 * n
        for row, seats in reserved.items():
            left_clear = not bool({2, 3, 4, 5} & seats)
            right_clear = not bool({6, 7, 8, 9} & seats)
            middle_clear = not bool({4, 5, 6, 7} & seats)
            
            if left_clear and right_clear:
                continue
            elif left_clear or right_clear or middle_clear:
                answer -= 1
            else:
                answer -= 2
                
        return answer