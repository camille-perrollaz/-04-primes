from math import sqrt

#### Fonction secondaire


def isprime(p):
    if p<2:
        return False
    for d in range(2,p):
        if p % d == 0:
            return False
    return True  

    pass

#### Fonction principale


def main():

    print(isprime(21))
    print(isprime(35))
    print(isprime(13))
    print(isprime(1))
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
