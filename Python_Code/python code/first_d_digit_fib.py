# Recall that the Fibonacci Numbers are defined as follows:

# 𝐹0=0,𝐹1=1 and 𝐹𝑛:=𝐹𝑛−1+𝐹𝑛−2 for 𝑛>1

# Write a Python function called first_D_digit_Fib that takes an integer argument D less
# than 30 and returns the first D-digit Fibonacci number.

# Test cases
# print(first_D_digit_Fib(2))
# 13

# print(first_D_digit_Fib(3))
# 144

# print(first_D_digit_Fib(8))
# 14930352

#print(first_D_digit_Fib(14))
#10610209857723

#print(first_D_digit_Fib(28))
#1066340417491710595814572169

def first_D_digit_Fib(d):
    if d == 1:
        return 0
    f0 = 0
    f1 = 1
    while True:
        f = f0 + f1
        f0 = f1
        f1 = f
        if len(str(f))==d:
            return f;
