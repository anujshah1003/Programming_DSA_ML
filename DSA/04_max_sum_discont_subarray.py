# -*- coding: utf-8 -*-

'''
This Question is from hackerrank. given an array find the maximum sum 
subarray 
This is similar to prevous problem but now the condition is that the max 
subarray need not be continuous

Example
array=[-1,2,3,-4,5,10]

The maximum subarray sum is comprised of elements at inidices 1,2,4 and 5.
Their sum is 2+3+5+10=20.

Solution 
We will use dynamic programming. we wil be using the previous result to compute
the current max.

in teh previous soution
current_max=max(prev_max+current_value,current_val) because wee need to get the
continuous array

For this problem as discontinuity is allowed

current_max=max(prev_max,prev_max+current_value,current_val) 

'''

#Time Complexity : O(N)
# Space Complexity : O(1)

def max_sum_discont_subarray(array):
    if len(array)<2:
        return array
    
    prev_max=array[0]
    overall_max=array[0]
    
    for i in range(1,len(array)):
        current_value=array[i]
        current_max=max(prev_max,prev_max+current_value,current_value)
        if current_max>overall_max:
            overall_max=current_max
        prev_max=current_max
        
    return overall_max

array_1=[-1,2,3,-4,5,10]
array_2=[1,-1,-1,-1,-1,5]

print(max_sum_discont_subarray(array_1))
print(max_sum_discont_subarray(array_2))
