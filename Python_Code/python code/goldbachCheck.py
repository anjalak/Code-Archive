#Recall that the Goldbach Conjecture states that any even number 𝑁 greater than 2 may be written as the sum of two primes.
# In this exercise you will write some code to verify this hypothesis (for moderately sized values of 𝑁).



# Write a Python function called 𝚐𝚘𝚕𝚍𝚋𝚊𝚌𝚑𝙲𝚑𝚎𝚌𝚔 that takes an even integer argument 𝑁 and returns a tuple (𝑝,𝑞) such that
# 𝑝+𝑞=𝑁 ordered such that 𝑝≤𝑞.



# Example: 𝚐𝚘𝚕𝚍𝚋𝚊𝚌𝚑𝙲𝚑𝚎𝚌𝚔(12)=(5,7)

# Example: 𝚐𝚘𝚕𝚍𝚋𝚊𝚌𝚑𝙲𝚑𝚎𝚌𝚔(1234)=(3,1231)


# This problem has a timeout limit of 1 second and a memory usage limit of 1MB, so be sure to write semi-efficient code!
#Each input in the test cases will satisfy 4≤𝑁≤1000000.

import math
def goldbachCheck(num):
    root = int(num/2);
    for i in range(2, root+1):
        if(isPrime(i)):
            if(isPrime(num-i)):
                return(i, num-i);

def isPrime(x):
    if(x == 1):
        return True;
    if x==2:
        return True;
    for i in range(2,x):
        if(x%i == 0):
            return False;
    return True;
