def numbersWith3Divisors(number: int):
    prime = [True]*(number+1)
    prime[0] = prime[1] = False
    p = 2
    while (p*p <= number):
 
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p*2, number+1, p):
                prime[i] = False
        p += 1
 
    i = 0
    count = 0
    while (i*i <= number):
        if (prime[i]):
            count = count + 1
        i += 1

    return count

print(f"Count of numbers with exactly 3 divisors is {numbersWith3Divisors(96)}") 

