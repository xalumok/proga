from calculator import calc

def generator(begin, end, step, EPS):
    if EPS <= 0 or begin > end or step <= 0:
        raise ValueError("Bad input")
    cur = begin
    while cur < end:
        yield calc(cur, EPS)
        cur += step