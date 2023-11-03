
# эту функцию можно использовать для правильного употребления секунд, минут, часов, дней, недель месяцев и не только


def choose_plural(x, words):
    
    if 5 <= x <= 20 or 5 <= x % 10 <= 9 or x % 10 == 0 or 11 <= x % 100 <= 20:
        return words[2]
    elif x == 1 or x % 10 == 1:
        return words[0]
    else:
        return words[1]
