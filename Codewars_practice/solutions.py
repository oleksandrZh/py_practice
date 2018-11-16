from math import sqrt


def song_decoder(song):
    result = str(song).replace("WUB", " ")
    while "  " in result:
        result = result.replace("  ", " ")
    return result.strip()


def find_next_square(sq):
    if round(sqrt(sq), 2) ** 2 == sq:
        return (sqrt(sq) + 1) ** 2
    else:
        return -1


def is_triangle(a, b, c):
    if (a + b > c) and (b + c) > a and (a + c) > b:
        return True
    else:
        return False


def to_camel_case(text):
    result = str(text).replace('_', '-').split('-')
    rs = result[0]
    for i in range(1, len(result)):
        rs = rs + result[i].capitalize()
    return rs


def divisors(integer):
    list_res = list()
    for i in range(2, integer):
        if integer % i == 0:
            list_res.append(i)
    if len(list_res) > 1:
        return list_res
    else:
        return str(integer) + " is prime"
