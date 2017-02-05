def merge_sort(A):
    '''
    INPUT: An array A of unsorted elements (integers). Assume n = 2^k
    OUTPUT: Sorted array A
    Comments: Divide, conquer, then merge. Runtime of O(n log n).
        T(n) = 2T(n/2) + O(n)
    '''

    length = len(A)
    # Base case
    if length is 1:
        return A
    else :
        # Divide
        midpoint = length // 2
        sub_1 = A[0:midpoint]
        sub_2 = A[midpoint:length]
        
        # Conquer
        sorted_1 = merge_sort(sub_1)
        sorted_2 = merge_sort(sub_2)

        sorted_merge = merge(sorted_1, sorted_2)
        
        return sorted_merge


def merge(A, B):
    '''
    INPUT: Two arrays, A, B, which are sorted and size n/2
    OUTPUT: Array C, which is merged A and B
    '''
    C = []
    isSorted = False
    counter_a = 0
    counter_b = 0
    counter_c = 0
    while isSorted is False:
        if counter_a < len(A) and counter_b < len(B):
            if A[counter_a] < B[counter_b]:
                C.append(A[counter_a])
                counter_a += 1
            else:
                C.append(B[counter_b])
                counter_b += 1
        elif counter_a < len(A):
            C.append(A[counter_a])
            counter_a += 1
        elif counter_b < len(B):
            C.append(B[counter_b])
            counter_b += 1
        else:
            isSorted = True
    return C
