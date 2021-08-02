# -*- coding: utf-8 -*-

'''
This Question is from hackerrank. given an array find the maximum sum 
continuous subarray 

Example
array=[-1,2,3,-4,5,10]

The maximum subarray sum is comprised of elements at inidices 1 to 5 . 
Their sum is 2+3-4+5+10=16.

Solution 
We will use dynamic programming. we wil be using the previous result to compute
the current max.
This solution is also known as kadane's algorithm

'''
#Time Complexity : O(N)
# Space Complexity : O(1)

def max_sum_cont_subarray(array):
    if len(array)<2:
        return array
    
    prev_max=array[0]
    overall_max=array[0]
    
    for i in range(1,len(array)):
        current_value=array[i]
        current_max=max(prev_max+current_value,current_value)
        if current_max>overall_max:
            overall_max=current_max
        prev_max=current_max
        
    return overall_max

array_1=[-1,2,3,-4,5,10]
array_2=[1,-1,-1,-1,-1,5]

print(max_sum_cont_subarray(array_1))
print(max_sum_cont_subarray(array_2))
