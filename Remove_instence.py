#DAY_6
#Remove all instence of a value in the array

def remove(nums,n):
    i=0
    for j in range(len(nums)):
        if nums[j]!=n:
            nums[i]=nums[j]
            i+=1
    return i

nums=[0,1,1,3,1,2,1,0,2,4]
#numbeer of elements=10
n=int(input("Enter the number you want erase the instence of that in the list:"))
result=remove(nums,n)
print("Number of elements after removing all the instence of n is",result)
print("New array is:",nums[:result])