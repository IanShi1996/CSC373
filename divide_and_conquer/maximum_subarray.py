import math

'''
PROBLEM: Given an array of integers, find the contiguous subarray which
results in the largest sum of its constituent integers.

INPUT: An integer array of size n, which potentially contain negative values

OUTPUT: Largest sub-array
'''

def naive_largest_subarray(A):
    '''
    Naive implementation, which results in O(n^2) runtime.
    '''
    max_sum = -math.inf
    indices = (0,0)
    
    for i in range(len(A)):
        running_sum = A[i]
        index_sum = A[i]
        index_indices = (i, i)
        
        for j in range(i+1, len(A)):
            running_sum += A[j]
            if running_sum > index_sum:
                index_sum = running_sum
                index_indices = (i, j)
                
        if index_sum > max_sum:
            max_sum = index_sum
            indices = index_indices
            
    return A[indices[0]:indices[1]+1]

def divide_and_conquer_largest_subarray(A, left, right):
    '''
    Divide and conquer implentation, which results in O(nlogn) runtime.
    '''
    # Base case: Conquer
    if (right - left) == 1:
        return (A[left], left, right)
    
    # Divide - for this implementation, assume array is always size 2^n
    midpoint = (right - left) // 2
    l_max = divide_and_conquer_largest_subarray(A, left, left + midpoint)
    r_max = divide_and_conquer_largest_subarray(A, left + midpoint, right)
    c_max = cross_max(A, left, left+midpoint, right)
    
    # Merge - choose the largest of l_max, r_max, c_max
    if l_max[0] > c_max[0] and l_max[0] > r_max[0]:
        return (l_max[0], l_max[1], l_max[2])
    elif r_max[0] > c_max[0] and r_max[0] > l_max[0]:
        return (r_max[0], r_max[1], r_max[2])
    else:
        return (c_max[0], c_max[1], c_max[2])

def cross_max(A, left, midpoint, right):
    '''
    Merge helper, which find the largest subarray which spans across the midpoint
    '''
    left_sum = -math.inf
    right_sum = -math.inf
    running_left_sum = 0
    running_right_sum = 0
    left_bound = midpoint
    right_bound = midpoint

    for i in range(midpoint, left - 1, -1):
        running_left_sum += A[i]
        if running_left_sum > left_sum:
            left_sum = running_left_sum
            left_bound = i
            
    for j in range(midpoint, right):
        running_right_sum += A[j]
        if running_right_sum > right_sum:
            right_sum = running_right_sum
            right_bound = j
            
    return (left_sum + right_sum, left_bound, right_bound + 1)

if __name__ == "__main__":
    # Expected output: [10, 19, 2, 20]
    test_array_1 = [10, 19, 2, 20]

    # Expected output: [22]
    test_array_2 = [-1, 22, -1, -1]

    # Expected output: [10, -1, 14]
    test_array_3 = [10, -1, 14, -1]

    # Expected output: [-1]
    test_array_4 = [-4, -1, -6, -7]

    '''
    test_out_1 = naive_largest_subarray(test_array_1)
    test_out_2 = naive_largest_subarray(test_array_2)
    test_out_3 = naive_largest_subarray(test_array_3)
    test_out_4 = naive_largest_subarray(test_array_4)
    '''

    test_out_5 = divide_and_conquer_largest_subarray(test_array_1, 0, len(test_array_1))
    test_out_6 = divide_and_conquer_largest_subarray(test_array_2, 0, len(test_array_2))
    test_out_7 = divide_and_conquer_largest_subarray(test_array_3, 0, len(test_array_3))
    test_out_8 = divide_and_conquer_largest_subarray(test_array_4, 0, len(test_array_4))

    '''
    print(test_out_1)
    print(test_out_2)
    print(test_out_3)
    print(test_out_4)
    '''

    print(test_array_1[test_out_5[1] : test_out_5[2]])
    print(test_array_2[test_out_6[1] : test_out_6[2]])
    print(test_array_3[test_out_7[1] : test_out_7[2]])
    print(test_array_4[test_out_8[1] : test_out_8[2]])
