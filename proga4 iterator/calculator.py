def calc(x, EPS):
    get_cur_elem = lambda x, n: ((-1)**(n+1))*(x**n)/n
    
    n=1
    res = 0
    while abs(get_cur_elem(x, n)) > EPS:
        res += get_cur_elem(x,n)
        n+=1
    return res