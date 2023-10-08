N = ord('A') % 10 + 1

print(N)


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def task_6():
    a, b = map(int, input().split())
    prime_numbers = [num for num in range(max(2, a), b + 1) if is_prime(num)]
    print(prime_numbers)


task_6()
