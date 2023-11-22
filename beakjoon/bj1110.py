def break_digit(num):
    if num >= 10:
        digit_2 = num//10
        num %= 10
        digit_1 = num//1
    else:
        digit_2 = 0
        digit_1 = num
    return digit_2, digit_1

class solution:
    def __init__(self, num):
        self.num = num
        self.result = 1e9
        self.cycle = 0

        self.result_bottom_end_calcy = num

    def calcy(self):
        numdigit_2, numdigit_1 = break_digit(self.num)
        while self.num != self.result:
            front = numdigit_1
            _, back = break_digit(numdigit_2 + numdigit_1)
            self.result = front * 10 + back

            numdigit_2, numdigit_1 = break_digit(self.result)
            self.cycle += 1
        
        print(self.cycle)
    
    def bottom_end_calcy(self):
        while True:
            resultdigit2, resultdigit1 = break_digit(self.result_bottom_end_calcy) 
            front = resultdigit1
            _, back = break_digit(resultdigit2 + resultdigit1)
            self.result_bottom_end_calcy = front * 10 + back

            self.cycle += 1
            if self.num == self.result_bottom_end_calcy:
                break 
        print(self.cycle)


num = int(input())

obj = solution(num)
# obj.calcy()
obj.bottom_end_calcy()