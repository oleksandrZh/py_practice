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


def encrypt(text, n):
    if n <= 0:
        return text
    else:
        result = text
        for i in range(0, n):
            first_part = ""
            second_part = ""
            index = 0
            for ch in result:
                index += 1
                if index % 2 == 0:
                    first_part += ch
                else:
                    second_part += ch
            result = first_part + second_part
        return result


def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    else:
        result = encrypted_text
        arr = list(encrypted_text)
        for i in range(0, n):
            split = len(result) // 2
            arr[1::2], arr[::2] = arr[:split], arr[split:]
        return ''.join(arr)


def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = p0 + p0 * percent / 100 + aug
        year += 1
    return year


def is_prime(num):
    result = list()
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num + 1):
            if num % i == 0:
                result.append(i)
    if len(result) >= 2:
        return False
    else:
        return True


def duplicate_count(text):
    result = list()
    text = text.upper()
    for ch in range(0, len(text)):
        for i in range(ch + 1, len(text)):
            if text[ch] == text[i] and text[ch] not in result:
                result.append(text[ch])
    return len(result)


def anagrams(word, words):
    result = list()
    for w in words:
        if ''.join(sorted(w)) == ''.join(sorted(word)):
            result.append(w)
    return result


def cakes(recipe, available):
    products = recipe.keys()
    multiples = list()
    for prod in products:
        recipe_value = recipe.get(prod)
        if available.get(prod) is None:
            available_value = 0
        else:
            available_value = available.get(prod)
        multiples.append(available_value // recipe_value)
    return min(multiples)


def find_missing(sequence):
    res = set()
    result = list()
    for i in range(1, len(sequence)):
        res.add(sequence[i] - sequence[i - 1])
    result.append(sequence[0])
    for i in range(0, len(sequence)):
        result.append(result[-1] + min(res))
    return (set(result) - set(sequence)).pop()


def rgb(r, g, b):
    values = list()
    values.append(r)
    values.append(g)
    values.append(b)

    for i in range(0, len(values)):
        if values[i] <= 0:
            values[i] = (hex(0).split('x')[-1])
        else:
            if values[i] >= 255:
                values[i] = (hex(255).split('x')[-1])
            else:
                values[i] = (hex(values[i]).split('x')[-1])

    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    result = ""

    for i in values:
        if i[0] in letters or i[-1] in letters:
            result = result + i.upper()
        else:
            if int(i) < 10:
                result = result + "0" + i
            else:
                result += i
    return result


"""def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num
    
def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))"""
