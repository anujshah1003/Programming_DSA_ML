# -*- coding: utf-8 -*-
'''
This is a question from interview query
You have an array of integers of length n spanning 0 to n with one missing. Write a function that returns the missing number in the array.

Example:

nums = [0,1,2,4,5] 
missingNumber(nums) -> 3
Complexity of O(N) required.

'''
# there are multiple wasy to solve the problem Some of th solutions provided by others
# are mentioned here 

# solution 1
# compare the indices with the corresponding value and if they are not same that 
# index is the missing number

def missing_number(nums):
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return 0
    
print(missing_number([0,1,2,4,5]))
print(missing_number([1,2,3,4,5]))
print(missing_number([0,1,2,3,4,5,7]))

# solution -2 
# use xor operation, between ondices and the value, the missing all the values
# will become 0 and the missing number would remain as x^x=0 and x^0=x
def missing_number(nums):
    result=0
    for i in range(1,len(nums)+1):
        result=result^nums[i-1]
        result=result^i
    return result
    
print(missing_number([0,1,2,4,5]))
print(missing_number([1,2,3,4,5]))
print(missing_number([0,1,2,3,4,5,7]))

# solution-3
#use mathematical formulation
# sum upto n numbers = n(n+1)/2

def missing_number(nums):
    n=len(nums)
    total_sum=n*(n+1)/2
    missing_num=total_sum-sum(nums)
    return missing_num

print(missing_number([0,1,2,4,5]))
print(missing_number([1,2,3,4,5]))
print(missing_number([0,1,2,3,4,5,7]))

# solution-4
# subtract each number from the previous number and if its not one then we find the
# missing number
def missing_number(nums):
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]!=1:
            return nums[i]-1
    return 0
print(missing_number([0,1,2,4,5]))
print(missing_number([1,2,3,4,5]))
print(missing_number([0,1,2,3,4,5,7]))



