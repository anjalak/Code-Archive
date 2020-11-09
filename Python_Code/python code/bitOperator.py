# Create a function in Python called bitOperator that takes two bit strings of length 5 from the user.

# The function should return a tuple of the bitwise OR string, and the bitwise AND string
# (they need not be formatted to a certain length, see examples).

def bitOperator(int1, int2):
    num1 = int(int1,2);
    num2 = int(int2,2);

    str1 = format(num1|num2,'b');
    str2 = format(num1&num2,'b');

    ans = (str1,str2);
    return ans;

# Test cases
# 1.
# result = bitOperator('01001','00100')
# possible_solution_1 = ('1101', '0')
# possible_solution_2 = ('01101', '00000')

# print (result==possible_solution_1 or result==possible_solution_2)
# True

# 2.
# result = bitOperator('10001', '11011')
# solution = ('11011', '10001')

# print (result==solution)
# True

# 3.
# result = bitOperator('11001', '11100')
# solution = ('11101', '11000')

# print (result==solution)
# True
