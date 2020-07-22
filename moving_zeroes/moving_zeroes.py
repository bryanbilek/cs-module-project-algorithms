'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # move the zeros to the right side
    # could try popping the zeros out & appending them at the end
    zeros = []

    for x in arr:
        if x == 0:
            arr.pop(x)
            print(arr)
            zeros.append(x)
            print(zeros)

    return arr.extend(zeros)


            


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")