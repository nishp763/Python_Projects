def get_prime_factors(N):
    prime_factors = list() # initialize empty list
    divisor = 2 # prime number is greater then 1 and not equal to 1
    
    while (N >= divisor):
        if (N%divisor == 0): # if even divide by 2
            N = (int) (N/divisor) # carry out division convert to int
            prime_factors.append(divisor) # add to our list
        else:
            divisor += 1 # increment divisor
    
    return prime_factors # return list


if __name__ == "__main__":
    print(get_prime_factors(630))
    print(get_prime_factors(13))