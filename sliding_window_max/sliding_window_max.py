'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # k represents the number of values starting at index 0 & returns the max value
    # then k moves at the same size one index over
    # slice through nums 
    start = 0
    end = k
    window = nums[start:end]

    while end != len(nums):
        m = max(window)
        start += 1
        end += 1
    
    return m
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
