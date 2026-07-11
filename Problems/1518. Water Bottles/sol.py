class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinks = 0

        while numBottles >= numExchange:
            remainder = (numBottles % numExchange)
            drink = numBottles - remainder
            drinks += drink
            new = numBottles // numExchange
            numBottles = new + remainder

        return drinks + numBottles