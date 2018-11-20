def plus(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


def minus(*args):
    summ = 2*args[0]
    for i in args:
        summ -= i
    return summ
