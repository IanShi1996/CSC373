'''
==========================================================================
PROBLEM: Given an unsorted array of integers of size n, find the majority
         integer value in the array. An integer is a majority when at
         least (n/2) + 1 elements of the array are that integer.
         This must be done without sorting.

INPUT: Integer array of size n. Assume n is a power of 2.

OUTPUT: Majority integer, and number of occurences
==========================================================================
'''

def majority_array(A):
    # Guard
    if not A or len(A) is 1:
        return None
        
    # Base Case / Conquer
    if (len(A) == 2):
        if (A[0] == A[1]):
            return [A[0], 2]
        else:
            return None
    # Divide
    left = A[0 : len(A) // 2]
    right = A[len(A) // 2 : len(A)]

    left_majority = majority_array(left)
    right_majority = majority_array(right)

    # Merge
    if left_majority:
        for integer in right:
            if integer == left_majority[0]:
                left_majority[1] += 1
        if left_majority[1] > len(left):
            return left_majority
    if right_majority:
        for integer in left:
            if integer == right_majority[1]:
                right_majority[1] += 1
        if right_majority[1] > len(right):
            return right_majority
    return None

'''
==========================================================================
Logic: If elements are not at least occupying half of a sub-array or both
       sub-arrays are the same, they cannot become the majority. Otherwise,
       we check the other sub-array for occurences of majority element.

Runtime: The merge step takes n/2 iterations to check if a majority
         candidate exists in the opposite sub-array.
         Recurrence relation is: 2T(n/2) + O(n).
         By Master's theorem, this equates with an O(nlogn) runtime.
==========================================================================
'''

if __name__ == "__main__":
    test_array_1 = [3, 2, 3, 3]
    test_array_2 = [1, 1, 1, 1]
    test_array_3 = [3, 2, 3, 1]
    test_array_4 = [3, 2, 3, 3, 1, 1, 1, 1]
    test_array_5 = [3, 2, 3, 3, 1, 1, 1, 3]
    test_array_6 = [3, 2, 3, 3, 1, 3, 1, 3]
    test_array_7 = [3, 3, 3, 3, 3, 4, 4, 4]
    test_array_8 = [3, 3, 3, 4, 4, 4, 4, 4]
    
    print(majority_array(test_array_1))
    print(majority_array(test_array_2))
    print(majority_array(test_array_3))
    print(majority_array(test_array_4))
    print(majority_array(test_array_5))
    print(majority_array(test_array_6))
    print(majority_array(test_array_7))
    print(majority_array(test_array_8))
