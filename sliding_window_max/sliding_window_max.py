'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # need an empty array to hold new values based on k value
    max_size = []
    # need an index so we can go through and set the highest number to it
    index = 0
    # while loop to append values to new array
    while index + k <= len(nums):
        # find the max number in sliced array
        max_size.append(max(nums[index:(k + index)]))
        #increase index by one so we can move the slider
        index += 1
    return max_size


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
