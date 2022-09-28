# return true if number is not prime
def find_if_not_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return True
    return False


def main():
    # find all prime numbers between 2 and 20
    for x in range(2, 20):
        if find_if_not_prime_number(x) is False:
            print(f'{x} is prime')


if __name__ == "__main__":  # pragma: no cover
    main()
