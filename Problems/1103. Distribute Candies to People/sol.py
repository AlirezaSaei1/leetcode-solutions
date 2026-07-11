class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        k = int((math.sqrt(1 + 8 * candies) - 1) // 2)
        total_given = k * (k + 1) // 2
        leftover = candies - total_given
        
        res = [0] * num_people

        for i in range(num_people):
            m = (k - i + num_people - 1) // num_people
            if m > 0:
                res[i] = m * (i + 1) + num_people * m * (m - 1) // 2

        if leftover > 0:
            res[k % num_people] += leftover
        
        return res