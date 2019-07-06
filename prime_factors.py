def prime_factors(number):
    var = 2
    factors = []
    while var * var <= number:
        if number % var:
            var += 1
        else:
            number //= var
            factors.append(var)
    if number > 1:
        factors.append(number)
    return factors


if __name__ == "__main__":
    n = 22
    print(prime_factors(n))  # 2, 11
