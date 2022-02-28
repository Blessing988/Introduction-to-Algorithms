"""
Pseudocode:

for j=2 to A.length
    key = A[j]
    // Insert A[j] into the sorted sequence A[1...j-1]
    i = j-1
    while i>0 and A[j] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i+1] = key
"""

def insort(a_list):
    """
    Takes the list to sort and 
    returns the version of the sorted list
    """
    # loop through the list starting from the second element
    for j in range(1, len(a_list)):
        # Getting the target number
        key = a_list[j]
        i = j-1
        while i >=0 and a_list[i] > key:
            a_list[i+1] = a_list[i]
            i = i-1
        a_list[i+1] = key

    return a_list

print(insort([5, 2, 4, 6, 2, 1, 3]))


