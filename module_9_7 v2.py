def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result):
            if result % i == 0:
                return f'Составное \n{result}'
        else:
            return f'Простое \n{result}'

    return wrapper

@is_prime
def sum_three(*args):
    summa = sum(list(args))
    return summa
    print(summa)


result1 = sum_three(2, 3, 6)
print(result1)

result2 = sum_three(2, 3, 5)
print(result2)
