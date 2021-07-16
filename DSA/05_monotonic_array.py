# -*- coding: utf-8 -*-
'''
This question is from https://www.geeksforgeeks.org/python-program-to-check-if-given-array-is-monotonic/
Given an array A containing n integers. The task is to check whether the array 
is Monotonic or not. An array is monotonic if it is either monotone increasing 
or monotone decreasing.

Als note that montone can have equal numbers that is

-3,1,1,1,3,5 is montinically increassing
10,9,8,8,7,7,1 is monotonically decreasing

They have provided a solution in their website :
# Check if given array is Monotonic
def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
    
Although the time complexty is o(n) the actual time complexity is o(n+n)

can we do it in just one pass actual o(n). also we can break as soon as we find out
that it is not a monotne , why to loop over remaining elements if we alredy know    

Teh solution is simple just find out what is teh nature of teh series
if it is decreainsg then check array[i]<=array[i-1] and if it is increasing
the array[i]>=array[i-1]
'''

# time complexity : O(n)
# space complexity: O(1)
def check_montonic_array(array):
    
    if len(array)<2:
        return True
    
    is_monotonic=True
    is_increasing=False
    is_decreasing=False
    
    for i in range(1,len(array)):
        # find the nature of teh series
        if not is_increasing and not is_decreasing:
            if array[i]==array[i-1]:
                continue # we still don't know the nature of the series
            elif array[i]>array[i-1]:
                is_increasing=True
            else:
                is_decreasing=True
                
        # if the nature was increasing and the ith element is less than i-1th elem
        # return False 
        if array[i]<array[i-1] and is_increasing:
            return False
        # if the nature was deccreasing and the ith element is greater than i-1th elem
        # return False 
        if array[i]>array[i-1] and is_decreasing:
            return False
        
    return is_monotonic
        
assert(check_montonic_array([1])==True)
assert(check_montonic_array([1,2,3,3,2,2])==False)
assert(check_montonic_array([0,0,-2,-3,-4,-5])==True)
assert(check_montonic_array([-3,-2,0,-1])==False)