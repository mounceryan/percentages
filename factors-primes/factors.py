def factor_checker(number):
    factors = 0
    for i in range(2, number):
        y = (number % i)
        if y == 0:
            factors = " is a factor of your number."
            print(str(i) + factors)   
factor_checker(int(input()))