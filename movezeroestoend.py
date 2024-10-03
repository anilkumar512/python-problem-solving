def moveZeroes(nums):
        nonzero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nonzero]=nums[i]
                nonzero+=1
            
        
        for i in range(nonzero,len(nums)):
            nums[i]=0
      
        return nums
nums=[2,0,6,0,4,0,9]
r=moveZeroes(nums)
print(r)
