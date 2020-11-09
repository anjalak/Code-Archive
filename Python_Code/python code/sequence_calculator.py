# Consider the recurrence relation 𝑎𝑛=𝑛2𝑎𝑛−1−𝑎𝑛−2 with initial conditions 𝑎0=1 and 𝑎1=2.

# Write a Python function called sequence_calculator that takes a nonnegative integer argument 𝑁
# less than 50 and returns the 𝑁-th term in the sequence defined by the above recurrence relation.

# For example, if 𝑁=2, your function should return sequence_calculator(2) = 7, because 𝑎𝑁=𝑎2=(2)2⋅(2)−(1)=7.
def sequence_calculator(num):
    if num == 0:
        return 1;
    elif num == 1:
        return 2;
    else:
        return num*num*sequence_slayer(num - 1) - sequence_slayer(num - 2);
