class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def palindrome(n):
            b = bin(n)[2:]
            return b == b[::-1]

        answer = []
        for num in nums:
            distance = 0

            while True:
                if num - distance > 0 and palindrome(num - distance):
                    answer.append(distance)
                    break

                if palindrome(num + distance):
                    answer.append(distance)
                    break

                distance += 1

        return answer