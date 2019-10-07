# Numeric Algorithms
# Contributed by: JordaoA

#Sieve of Eratosthenes implemented in python

def cieve(rangeOfPrimes):
    try:    
        rangeOfPrimes = int(rangeOfPrimes)
        primes = []

        if rangeOfPrimes < 2:
            return("invalid Range :(")

        elif rangeOfPrimes == 2:
            primes.append(2)
            return(primes)

        else:
            cieve = [True] * rangeOfPrimes
            cieve[0] = False
            cieve[1] = False

            for i in range(2,rangeOfPrimes):
                if cieve[i]:
                    for j in range(i*2,rangeOfPrimes,i):
                        cieve[j] = False
            
            for i in range(rangeOfPrimes):
                    if cieve[i]:
                        primes.append(i)

            return(primes)

    except:
        return("invalid Type :(")
