'''
this is a problem from daily coding interview - https://www.dailycodingproblem.com/
I recived this question as I have sun=bscribed for recieveing mail

Given a list of integers and a number K, return which contiguous elements of 
the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return 
[2, 3, 4], since 2 + 3 + 4 = 9.

'''

# Time complexity o(n) + o(n) = the fisrt o(n) is to loop over tha array
# the second time that is in while loop it is not looping over all elemnet, the 
# element ehihc have been removed from the list are not vistided so through out 
# we just visit o(n) hence the time complexity o(n)+o(n)

# space complexity o(n)

def find_contiguous_elem_sums_to_k(array,k):
    
    # define a queue like data structure, pop from front
    contiguous_elem=[]
    
    sum_=0
    for i in range(0,len(array)):
        
        sum_+=array[i]
        if sum_==k:
            contiguous_elem.append(array[i])
            return contiguous_elem
        elif sum_<k:
            contiguous_elem.append(array[i])
        elif sum_>k:
            contiguous_elem.append(array[i])
            while sum_>k and len(contiguous_elem):
                remove=contiguous_elem.pop(0)
                sum_-=remove
            if sum_==k:
                return contiguous_elem
            
    if sum_!=k:
        return []
    
array=[1, 2, 3, 4, 5]
k=9

print(find_contiguous_elem_sums_to_k(array,k))

print(find_contiguous_elem_sums_to_k([1,2,3,4,5],4))

print(find_contiguous_elem_sums_to_k([1,2,-3,4,5],4))

print(find_contiguous_elem_sums_to_k([5],5))
print(find_contiguous_elem_sums_to_k([1,2],14))