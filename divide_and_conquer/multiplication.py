def naive_multiplication(X, Y):
    '''
    INPUT: X, Y, which are n digit integers
    OUTPUT: X * Y
    Comments: Using the elementary school algorithm.
        Using the number of 1 digit multiplications as a step.
        Expecting a runtime of O(n^2).
    '''

    X = str(X)
    Y = str(Y)
    total_sum = 0
    for x_digit in range(len(X)-1, -1, -1):
        column_sum = 0
        for y_digit in range(len(Y)-1, -1, -1):
            column_sum += 10 ** ((len(Y) - 1) - y_digit) * int(X[x_digit]) * int(Y[y_digit])
        total_sum += column_sum * 10 ** ((len(X) - 1) - x_digit)

    # Results in n^2 single digit operations
    return total_sum

def naive_multiplication_divide(X, Y):
    '''
    INPUT: X, Y, which are n digit integers. Assume n = 2^k
    OUTPUT: X * Y
    Comments: Using recursive divide and conquer. Still runs in O(n^2), with a
        recurrence of T(n) = 4T(n/2) + O(1) which is in O(n^2)
    '''
    X = str(X)
    Y = str(Y)
    # Assume n = 2^k, len(X) == len(Y)    
    length = len(X)
    # Base case
    if (length is 1):
        return int(X) * int(Y)
    else:
        total_sum = 0
        # We divide number into two halves
        midway = length // 2
        x_1 = int(X[0:midway])
        x_2 = int(X[midway:len(X)])
        y_1 = int(Y[0:midway])
        y_2 = int(Y[midway:len(Y)])
        
        result_1 = naive_multiplication_divide(x_1, y_2) * 10 ** midway
        result_2 = naive_multiplication_divide(x_1, y_1) * 10 ** length
        result_3 = naive_multiplication_divide(y_1, x_2) * 10 ** midway
        result_4 = naive_multiplication_divide(y_2, x_2)

        return result_1 + result_2 + result_3 + result_4

def karatsuba_multiplication(X, Y):
    '''
    INPUT: X, Y, which are n digit integers. Assume n = 2^k.
    OUTPUT: X * Y
    Comments: Using Karatsuba's algorithm; we can get runtime O(n^log_2(3)).
        This is because we reduce the number of recursions, making it
        T(n) = 3T(n/2) + O(1) which is in O(n^log_2(3)) by Master's Thm
    '''
    X = str(X)
    Y = str(Y)
    # Assume n = 2^k, len(X) == len(Y)    
    length = len(X)
    # Base case
    if (length is 1):
        return int(X) * int(Y)
    else:
        total_sum = 0
        # We divide number into two halves
        midway = length // 2
        x_1 = int(X[0:midway])
        x_2 = int(X[midway:len(X)])
        y_1 = int(Y[0:midway])
        y_2 = int(Y[midway:len(Y)])
        
        result_1 = naive_multiplication_divide(x_2, y_2)
        result_2 = naive_multiplication_divide(x_1, y_1)
        # Critical step
        result_3 = naive_multiplication_divide((y_1+y_2), (x_1+x_2))
        final_3 = result_3 - result_1 - result_2    
        return final_3 * 10 ** midway + result_1 + result_2 * 10 ** length 
