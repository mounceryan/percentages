def prime_checker(number):
    x = number
    prime = " is a prime."
    if number == 2:
        print(str(2) + prime)
    for i in range(2, number):
        y = (number % i)
        if y == 0:
            prime = " is not a prime."
            print(str(x) + prime)
            break
        elif y != 0:
            print(str(x) + prime)
            break

prime_checker(int(input()))