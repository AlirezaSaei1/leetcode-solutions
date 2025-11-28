class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz = []
        for i in range(1, n+1):
            by3 = i % 3
            by5 = i % 5

            if by3 == 0 and by5 == 0:
                fizzbuzz.append("FizzBuzz")
            elif by3 == 0:
                fizzbuzz.append("Fizz")
            elif by5 == 0:
                fizzbuzz.append("Buzz")
            else:
                fizzbuzz.append(str(i))
            
        return fizzbuzz