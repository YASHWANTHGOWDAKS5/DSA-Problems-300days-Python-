#day_3
#Maximum sum with a subarray from the main array
def Max(nums):
    current_sum=max_sum=nums[0]
    for i,num in enumerate(nums[1:]):
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
        return max_sum
nums=[-1,2,3,-1,-2,4,3,-3]
result=Max(nums)
print(result)
