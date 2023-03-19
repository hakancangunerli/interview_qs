'''
2. Search Insertion Point

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

EX1 :
  Input: nums = [1,3,5,6], target = 5
  Output: 2

EX2:
  Input: nums = [1,3,5,6], target = 2
  Output: 1

EX3:
  Input: nums = [1,3,5,6], target = 7
  Output: 4
  
'''


# binary search 
# list of integers -> nums, target -> int 
def insertionPoint(nums, target):

    left =0 
    right= len(nums) -1 
    while left <= right:
        if (left + right ) % 2 ==0:
            mid = (left + right) //2
        else: 
            mid = (left + (right -1))//2 
        
        if nums[mid] == target:  # if middle value, return the middle 
            return mid
        elif nums[mid] < target: # if less than middle value but left and right are the same 
            if left == right:
                return mid +1 # mid position +1 
            left =  mid +1 
        else:
            if left == right:
                return mid # if not, which means larger, return 
            right = mid

print(insertionPoint([1,3,5,6],0))


















# def FizzBuzz(n):
#     answer = []
#     for i in range(1,n+1):
#         if i % 3 ==0 and i % 5 ==0: # divisible by 3 and 5
#             answer.append("FizzBuzz")
#         elif i % 3 ==0: # divisible by 3 
#             answer.append("Fizz")
#         elif i % 5 ==0: # divisible by 5
#             answer.append("Buzz")
#         else:
#             answer.append(str(i))
#     return answer

# print(FizzBuzz(5))    



