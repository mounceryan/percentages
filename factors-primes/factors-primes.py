def factor_prime_checker(number):
    x = number
    prime = " is a prime."
    for i in range(2, number):
        y = (number % i)
        if y == 0:
            factors = " is a factor of your number."
            print(str(i) + factors)
            print(str(x) + " is not a prime.", end="\r")
        elif y != 0:
            print(str(x) + " is a prime.", end="\r")
            
factor_prime_checker(int(input()))