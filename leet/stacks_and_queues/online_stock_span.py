# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4667/

input = [100, 80, 60, 70, 60, 75, 85]

class StockSpanner:
    stocks = []
    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        counter = 0
        self.stocks.append(price)
        for i in range(len(self.stocks) - 1, -1, -1):
            if self.stocks[i] <= price:
                counter += 1
            else:
                break

        return counter
    

stocksSpanner = StockSpanner()
for item in input:
    print(stocksSpanner.next(item))

