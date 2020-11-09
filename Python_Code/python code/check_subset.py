#Write a Python function check_subset() that takes in two Python lists,
#representing sets of integers, 𝐴 and 𝐵. Your function should return a single Boolean
#(True or False) for whether or not either set is a subset of the other. 𝐴 and 𝐵 are sets,
# and not necessarily non-empty.
def check_subset(list1, list2):
    res = 1;
    if (len(list1) == 0):
        return True;
    set1 = set(list1);
    set2 = set(list2);
    return set2.issubset(set1);
