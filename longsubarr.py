def lenOfLongSubarr (arr, n, k) : 
    #Complete the function
    sum=0
    sub=[]
    for i in range(n):
        sum+=arr[i]
        sub.append(arr[i])
        if sum==k:
            return len(sub)

arr =[1,4,3,5,3]
n = len(arr)
k = 8
print(lenOfLongSubarr(arr, n, k))  

