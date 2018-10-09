def Euclid_gcd(n1, n2):
    dividend = max(n1, n2)
    divisor = min(n1, n2)

    while dividend > 0:
        if divisor == 0:
            return dividend
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder


print(Euclid_gcd(270, 192))
