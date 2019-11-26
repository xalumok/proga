from calculator import calc

class Iterator:
    def __init__(self, begin, end, step, EPS):
        if EPS <= 0 or begin > end or step <= 0:
            raise ValueError("Bad input")
        self.begin = begin
        self.end = end
        self.step = step
        self.EPS = EPS
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.begin < self.end:
            cur = calc(self.begin, self.EPS)
            self.begin += self.step
            return cur
        else:
            raise StopIteration

    
