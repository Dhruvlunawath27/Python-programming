def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d)**power for d in digits)

def armstrong_numbers_in_range(start, end):
    return [n for n in range(start, end + 1) if is_armstrong(n)]
    return num == sum(int(d)**power for d in digits)
