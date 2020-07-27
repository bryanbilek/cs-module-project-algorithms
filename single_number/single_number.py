'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    # find the int with a count of 1
    
    #O(n^2)
    for x in arr: # O(n) 
        if arr.count(x) == 1: # O(n)
            return x # O(1)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
