
'''
https://www.hackerrank.com/challenges/maxsubarray/problem
'''
#dynamic programming

def maxSubarray(arr):
    # Write your code here
    if len(arr)==1:
        return (arr[0],arr[0])
    prev_max=arr[0]
    overall_max=arr[0]
    
    for i in range(1,len(arr)):
        max_1=prev_max+arr[i]
        max_2=arr[i]
        current_max=max(max_1,max_2)
        if current_max>overall_max:
            overall_max=current_max
        prev_max=current_max
    
    overall_max_2=arr[0]  
    prev_max=arr[0]  
    for i in range(1,len(arr)):
        current_max=max(prev_max,prev_max+arr[i],arr[i])
        if current_max>overall_max_2:
            overall_max_2=current_max
        prev_max=current_max
            
    return (overall_max,overall_max_2)


print(maxSubarray([1]))
print(maxSubarray([-1,-2,-3,-4,-5,-6]))
print(maxSubarray([1,-2]))
print(maxSubarray([1,2,3]))
print(maxSubarray([-10]))
print(maxSubarray([1,-1,-1,-1,-1,5]))

#1 1
#-1 -1
#1 1
#6 6
#-10 -10
#5 6
#%%
#	prev_max=array[0]
#	overall_max=array[0]
#	for i in range(1,len(array)):
#		current_max=max(array[i]+prev_max,array[i])
#		if current_max>overall_max:
#			overall_max=current_max
#		prev_max=current_max
#			
#	return overall_max