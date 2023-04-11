def fibonacci_primes(min_range, max_range):
     
    def check_prime(min_range, max_range):

            prime_workings_list = []
            not_prime_workings_list = []
            
            if min_range < 2:
                prime_workings_list.append(2)
            
            a = min_range
            for a in range(min_range, max_range):
                for b in range(2, a):
                    c = (a % b)
                    if c == 0:
                        not_prime_workings_list.append(a)
                        break
                    elif c != 0:
                        prime_workings_list.append(a)
            a += 1

            prime_list = list(dict.fromkeys(d for d in prime_workings_list if d not in not_prime_workings_list))
            return prime_list
        
    def check_fibonacci(min_range, max_range):
            without_range_fibonacci_list = []
            a, b, c, d = 0, 1, 0, max_range
            while c < d:
                without_range_fibonacci_list.append(a)
                e = a + b
                a = b
                b = e
                c += 1
            with_range_fibonacci_list = [i for i in without_range_fibonacci_list if i > min_range and i < max_range]                    
            return with_range_fibonacci_list

    prime_list = check_prime(min_range, max_range)
    #print("Prime numbers between " + str(min_range) + " and " + str(max_range) + ": " + str(prime_list))

    fibonacci_list = check_fibonacci(min_range, max_range)
    #print("Fibonacci numbers between " + str(min_range) + " and " + str(max_range) + ": " + str(fibonacci_list))

    fibonacci_prime_list = list(dict.fromkeys(i for i in fibonacci_list if i in prime_list))
    print("Fibonacci prime numbers between " + str(min_range) + " and " + str(max_range) + ": " + str(fibonacci_prime_list))   

fibonacci_primes(int(input()), int(input()))