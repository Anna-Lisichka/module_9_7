
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result not in (-1, 0, 1) and result % 2 ==0:
            simple = result ==2
        else:
            d = 3
            while d * d <= result and result % d != 0:
                d += 2
            simple = d * d > result
            if simple:
                print('Простое')
            else:
                print('Составное')

        return result
    return wrapper
@is_prime
def sum_three(*args):
    summa = sum(list(args))
    return summa
    print(summa)

result = sum_three(2, 3, 6)
print(result)

