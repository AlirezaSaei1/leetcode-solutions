class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        total_tax = 0.0
        prev_upper = 0

        for upper, percent in brackets:
            if income <= prev_upper:
                break

            taxable_amount = min(income, upper) - prev_upper
            total_tax += taxable_amount * (percent / 100.0)
            prev_upper = upper

        return total_tax