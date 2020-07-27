'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # move the zeros to the right side
    # could try popping the zeros off, appending them to a new, empty array
    # then extend that new array to the current one

    for x in arr:
        if x == 0:
            arr.pop(arr.index(x))
            arr.append(x)
            print(arr)

    return arr           


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")