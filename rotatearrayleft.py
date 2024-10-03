def rotatearrayleft(nums, k):
    n = len(nums)
    k = k % n  
    # nums[:] = nums[-k:] + nums[:-k]
    # return nums
    nums_copy = nums[:]
    for i in range(n):
        new_position = (i + k) % n                                 
        nums[new_position] = nums_copy[i]
    return nums
list=[1,2,3,4,5,6,7]
print(rotatearrayleft(list,3))