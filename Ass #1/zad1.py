import sys

def prime_factors(n):
    factors = {}
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors[divisor] = count
        divisor += 1
    return factors

def format_output(number, factors):
    output = f"{number} = "
    for factor, power in factors.items():
        if power == 1:
            output += f"{factor}*"
        else:
            output += f"{factor}^{power}*"
    return output[:-1]

argv = sys.argv[1:]
for i in range(len(argv)):
    number = int(argv[i])
    factors = prime_factors(number)
    output = format_output(number, factors)
    print(output)
