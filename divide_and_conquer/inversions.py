'''
PROBLEM: Find the number of out-of-order elements in an array.
Elements are out-of-order when they deviate from an ascending sorted
list of integers.

Example: 1, 3, 4, 2 -> Out of order: (3, 2), (4, 2) -> Number of inversions: 2

INPUT: Array of integers of size n. Assume n is a power of 2.

OUTPUT: Number of inversions to return array to sorted state
'''

def inversions(A, left, right):
    # Base Case: Conquer
    if (len(A[left:right]) == 2):
        if A[left] > A[right-1]:
            A[left], A[right-1] = A[right-1], A[left]
            return 1
        else:
            return 0

    # Divide
    midpoint = (left + right) // 2

    right_invs = inversions(A, midpoint, right)
    left_invs = inversions(A, left, midpoint)

    # Merge
    merge_invs = merge_inversions(A, left, midpoint, right)

    return right_invs + left_invs + merge_invs

def merge_inversions(A, left, midpoint, right):
    left_array = A[left:midpoint]
    right_array = A[midpoint:right]
    num_inv = 0
    
    counter_l = 0
    counter_r = 0
    counter = left
    
    for i in range(right - left):
        if (counter_r == len(right_array)):
            A[counter] = left_array[counter_l]
            counter_l += 1
            
        elif (counter_l == len(left_array)):
            A[counter] = right_array[counter_r]
            counter_r += 1
            
        elif (right_array[counter_r] < left_array[counter_l]):
            num_inv += len(left_array) - counter_l
            A[counter] = right_array[counter_r]
            counter_r += 1
        else:
            A[counter] = left_array[counter_l]
            counter_l += 1
        counter += 1
    return num_inv

if __name__ == "__main__":
    test_array_1 = [0, 1, 2, 3]
    test_array_2 = [3, 2, 1, 0]
    test_array_3 = [7, 6, 5, 4, 3, 2, 1, 0]
    
    print(inversions(test_array_1, 0, len(test_array_1)))
    print(inversions(test_array_2, 0, len(test_array_2)))
    print(inversions(test_array_3, 0, len(test_array_3)))
    
