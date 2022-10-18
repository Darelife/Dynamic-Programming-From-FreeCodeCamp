# Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of 
# numbers as arguments.

# The function should return a boolean indicating whether or not it is possible to generate
# the targetSum using numbers from the array.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are nonnegative.

# example : canSum(7, [5,3,4,7]) -> True
#           3+4 or just 7 directly = 7

#           canSum(7, [2,4]) -> False
#           no combination of 2 and 4 can add up to 7

# Step 1: Visualize the problem as a tree
# head = 7 : Make different branches for each number in the array (subtract the number from the head)
# 7 - 5 = 2 : Make different branches for each number in the array (subtract the number from the head)
# 2 - 5 = -3 : This is a leaf node, it's not a valid combination
# 2 - 3 = -1 : This is a leaf node, it's not a valid combination
# 2 - 4 = -2 : This is a leaf node, it's not a valid combination
# 2 - 7 = -5 : This is a leaf node, it's not a valid combination
# 7 - 3 = 4 : Make different branches for each number in the array (subtract the number from the head)
# 4 - 5 = -1 : This is a leaf node, it's not a valid combination
# 4 - 3 = 1 : Make different branches for each number in the array (subtract the number from the head)
# 1 - 5 = -4 : This is a leaf node, it's not a valid combination
# 1 - 3 = -2 : This is a leaf node, it's not a valid combination
# 1 - 4 = -3 : This is a leaf node, it's not a valid combination
# 1 - 7 = -6 : This is a leaf node, it's not a valid combination
# 4 - 4 = 0 : This is a leaf node, it's a valid combination
# 7 - 4 = 3 : Make different branches for each number in the array (subtract the number from the head)
# 3 - 5 = -2 : This is a leaf node, it's not a valid combination

# and so on
# if any branch of a head returns True, then the head is True

#time to write the code now

def canSum(targetSum:int, numbers:list):
    if targetSum==0: return True
    if targetSum<0: return False
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers) == True:
            return True
    return False
    # will return false if everything else fails

print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
# print(canSum(300, [7,14])) #won't load cuz it's too slow


