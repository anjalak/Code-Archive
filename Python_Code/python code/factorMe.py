#Write a Python function 𝚏𝚊𝚌𝚝𝚘𝚛𝙼𝚎 that takes in a nonnegative semiprime number 𝙽 which is the product of
#two prime numbers 𝑝 and 𝑞 and returns the  tuple ( 𝑝, 𝑞 ) where 𝑝≤𝑞.

#Example: 𝚏𝚊𝚌𝚝𝚘𝚛𝙼𝚎(22)=(2,11)

#Example: 𝚏𝚊𝚌𝚝𝚘𝚛𝙼𝚎(3605282209)=(59447,60647)

#This problem has a time-out limit of 1 second and a memory limit of 1MB.
#The number 𝑁 in all test-cases will satisfy 4≤𝑁≤800000000000000



import math
def factorMe(num):
    root = math.sqrt(num);
    temp = math.ceil(root);
    if(temp*temp == num):
        return(temp, temp);
    while(temp > 1):
        if(num%temp == 0):
            return(temp, int(num / temp));
        temp = temp -1;
    return (temp, temp);
