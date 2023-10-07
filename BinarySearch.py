#painter partition problem

class Solution:
    def minTime (self, arr, n, k):
        def checktime(arr,m,k):
            ct=1
            sum1=0
            for i in arr:
                if i +sum1>m:
                    ct +=1
                    sum1=i
                    
                else:
                    sum1+=i
                    
            # if ct>k:
                # return False
            # return True
            return ct <=k
                
        l=max(arr)
        r=sum(arr)
        ans=r
        # r=0
        # l=float("-inf")
        # for i in range(n):
        #     l=max(l,arr[i])
        #     r=r+arr[i]
        while l<=r:
            m=(l+r)//2
            if checktime(arr,m,k):
            # if a :
                ans=m
                r=m-1
            else:
                l=m+1
        return ans
            
