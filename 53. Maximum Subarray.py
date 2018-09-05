#https://leetcode.com/problems/maximum-subarray/description/

#use recursive thinking to develop

# normal traverse all the sublists of list

curSum = maxSum = nums[0]
# to extend the length of sublists
for num in nums[1:]:
  # consider the all the sublists now(means when length of sublist = i), the maximum result
    curSum = max(num, num+curSum)
    print(curSum)
   # maxSum is to compare every curSum in different length of sublist
    maxSum = max(maxSum, curSum)
    print(maxSum)
print(maxSum)

"""
for example:
nums = [-2,1,-3,4,-2,2,1,-5,4]
first time is -2
length = 2: we should pick [1] instead of [-2,1] to attend later maximum  curSum=1, maxSum=1
length = 3: we should pick [1,-3] instead of -3 to attend, curSum =-2, maxSum still =1
length = 4: we should pick [4] instead of [1,-3,4] to attend, curSum = 4, maxSum = 4
length = 5: we should pick [4,-2] instead of [-2] to attend, curSum = 2, maxSum =4
length = 6: we should pick [4,-2,2] instead of [2] to attend, curSum = 4, maxSum= =4 
length = 7: we should pick [4,-2,2,1] instead of [1] to attend, curSum = 5, maxSum =5 
length = 8: we should pick [4,-2,2,1] instead of [-5]
length = 9: we should pick [4,-2,2,1] instead of 4

choose for now the considering number: num and num+curSum is a correct method
because curSum includes maximum result before, will I include new num will do good to curSum?
if new value added, that is num come in, it add effect makes curSum greater than num itself, just keep it include curSum situation
if num itself is bigger enough, it won't need previous help, 
the help from previous sublists hinder it becomes strong, the help always be negative, so I START FROM NOW again, take num as curSum
"""
