# This defines the function with the range variables which we are searching for primes between.
def prime_checker_range(low_range, high_range):
    # This creates an empty list called prime_workings_list.
    prime_workings_list = []
    # This creates an empty list called not_prime_workings_list.
    not_prime_workings_list = []
    # This sets the variable x to equal the low_Range variable.
    x = low_range
    # This is a for loop which takes x each time whilst it is within the range we have set and then executes the next for loop 
    # until it has done that for each integer in the range.
    for x in range(low_range, high_range):
        # This is a for loop which takes i each whilst it is in the range of 2 to x. This then executes the code in this for loop
        # until it gets to the top of our range. This is the for loop whose code is dividing each number in the range by the other 
        # numbers to see if they are prime for not.
        for i in range(2, x):
            # This is seeing if there is a ramainder left over when the x variable is divided by i. This indicates whether i is a factor of x or not.
            y = (x % i)
            # This is an if statement which executes the code on the next line if y is equal to 0, i.e. if there is no remainder when the calculation
            # above is done.
            if y == 0:
                # This appends the x variable to the not_prime_workings_list.
                not_prime_workings_list.append(x)
                break
            # This elif executes the code on the next line if y does not equal zero, so if there is something remaining after that calculation.    
            elif y != 0:
                # This appends the x variable to the prime_workings_list.
                prime_workings_list.append(x)
    # This increases the variable x by 1.
    x += 1
    
    #The two below lines of code are comments which if you get rid of the # returns a list of numbers which are not prime.
    #not_prime_list = list(dict.fromkeys(x for x in not_prime_workings_list if x in prime_workings_list))
    #print("List of numbers which are not prime: " + str(not_prime_list))
    
    # This defines the variable prime_list. The bi from 'x' onwards filters out numbers from the prime_workings_list which are already on the 
    # not_prime_workings_list. This is because the function divides each number by the numbers before it, e.g. 6/2 = 3 would add 6 to the 
    # not_prime_working_list, but 6/4 = 1.5 would add 6 to the prime_working_list because there is a remainder of 0.5 in the calculation even 
    # though it is not prime. This part of the line filters out these occurences so that the list only shows primes. 'dict.fromkeys' creates 
    # a dictionary, in layman's terms this means that the duplicates are removes from the list. 'List' makes this object into an actual list in Python.
    prime_list = list(dict.fromkeys(x for x in prime_workings_list if x not in not_prime_workings_list))

    # This prints a message plus the variable prime_list which is the list of prime numbers.
    print("List of prime numbers: " + str(prime_list))

prime_checker_range(int(input()), int(input()))

# Note that the list does not return the prime number 2.
