def sum_divisors(number):
    return sum([num for num in range(1, number) if number % num == 0])


def is_positive_int(number):
    return number > 0 and type(number) == int


def classify(number):
    if not is_positive_int(number):
        raise ValueError('number not a positive integer > 0')

    divisors_sum = sum_divisors(number)
    if divisors_sum > number:
        return "abundant"
    elif divisors_sum < number:
        return "deficient"
    else:
        return "perfect"
