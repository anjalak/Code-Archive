#Write a Python function 𝚖𝚎𝚛𝚐𝚎𝚂𝚘𝚛𝚝() that takes in a list of unique integers and, using the Merge Sort recursive algorithm
#(found on textbook page 368):

#1) Prints each comparison performed, in order.

#2) Returns the sorted list.

#When you print the comparisons, it should be in the format of 'low-number<high-number' as displayed in the examples.

import math
list_temp = []

def mergeSort(list5):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    if len(list5) > 1:
        m = (len(list5)//2)
        list1 = list5[:m]
        list2 = list5[m:]
        list3 = mergeSort(list1)
        list4 = mergeSort(list2)
    else:
        return list5
    return merge(list3,list4)

def merge(list3, list4):
    templist = []
    while(len(list3) > 0 and len(list4) > 0):
        if(list3[0] < list4[0]):
            templist.append(list3[0])
            print(str(list3[0]) + "<" + str(list4[0]))
            del list3[0]
        else:
            templist.append(list4[0])
            print(str(list4[0]) + "<" + str(list3[0]))
            del list4[0]
    for x in list3:
        templist.append(x)
    for x in list4:
        templist.append(x)
    list_temp = templist;
    return list_temp



    
