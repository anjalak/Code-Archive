# Write a Python function powerSet() that takes in a finite list object 𝐴 and returns P(𝐴),
#the power set of A. The output should be only in the form of list objects.

#Solution 1
def powerSet(list1):
    size = 2**len(list1)
    count = 0
    powerSetList = []
    for count in range(size):
        temp = []
        for i in range(len(list1)):
            if((count & (1 << i)) > 0):
                temp.append(list1[i])
        powerSetList.append(temp)
    return powerSetList

#solution 2
def powerSet2(A):
    return_set = [[]]
    for a in A:
        return_set.extend([existing_set + [a] for existing_set in return_set])
    return return_set
