def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    for num in range(2, n):
        if is_prime(num):
            print(num, end=' ')
    print()

def get_primes(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes