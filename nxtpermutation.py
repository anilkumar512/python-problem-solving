import itertools
def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        permutations=list(itertools.permutations(nums))
        
        return permutations[2]
list=[1,2,3]
print(nextPermutation(list))