print("Brute Force method of TWOSUM-(NOT EFFICIENT)")
print("1.day one of python DSA")
print("1.Two sum")
def TwoSum(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                return(i,j)

numbers=[2,4,5,3,2,1]
target=7
result=TwoSum(numbers,target)
print(result)

print("Lets use HashMap to get the optimal solution")
def TwoSum1(num,target):
    seen={}
    for i,nums in enumerate(num):
        diff=target-nums
        if diff in seen:
            return(seen[diff],i)
        seen[nums]=i

num=[2,4,5,3,2,1]
target=7
result=TwoSum(num,target)
print(result)