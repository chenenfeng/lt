#ascending array with some pivots, like[4,5,6,7,1,2,3], 1 is just the pivot, no duplicate exists
# time complexity should be O(logn)
# give a target number, then find the number in the array and return in its index, if not found, return -1

"""
I need to find the pivot, because no duplicate, if I use for-looper to compare number, the complexity if O(n)
binary search's time complexity is O(logn), 
find pivot is another job, if there is only a pivot, then I will make comparison between target with head and last value.
I think this problem only have 1 pivot.
looks like whatever i should use binary search for sorted array, the pivotal thing is to translate my list as the sorted list to binanry search
then just look at the target number in which side, in leftside, right side should be infinite, in rightside, left side shoud be -infinite
target value is 5, then [4,5,6,7,1,2,3] become [4,5,6,7,inf,inf,inf]
what is important is thatm, only the mid value refer to right side should assign inf to mid value
"""

#
low = 0
high = len(lists)-1
while(low <= high):
    mid = (low+high)//2
    if target > lists[0]:
        # mid is in the same side with target, accept mid value, just like normal binary search
        # be careful, mid is just index, I should use lists[mid] to make comparison
        # be another careful, is >= not > because I will make mistake on lists = [1,3]
        if lists[mid] >= lists[0]:
            mid_value = lists[mid]
        # mid is in another side, assign mid_value with Inf
        else:
            mid_value = float('Inf')
    elif target == lists[0]:
        return 0
    # target is in the right side, look at the mid position
    else: 
        if mid < lists[0]:
            mid_value = lists[mid]
        else:
            mid_value = -float('Inf')
    # now do the binary search
    if target == mid_value:
        return mid
    elif target < mid_value:
        high = mid-1
    else:
        low = mid+1
# don't find
return -1
          
