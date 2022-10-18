# Write a function howSum(targetSum, numbers) that takes in a targetSum and an array of
# numbers as arguments.

# The function should return an array containing any combination of elements that add up
# to exactly the targetSum. If there is no combination that adds up to the targetSum, then
# return null.

# If there are multiple combinations possible, you may return any single one.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are nonnegative.

# example : howSum(7, [5,3,4,7]) -> [3,4]
#           3+4 = 7

#           howSum(7, [2,4]) -> None
#           no combination of 2 and 4 can add up to 7


#? MY SOLUTION

def howSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None
    answers = []
    for num in numbers:
        remainder = targetSum - num
        if howSum(remainder, numbers) is not None:
            answers.append(num)
        a = targetSum
        for i in answers:
            a -= i
        if a == 0:
            return answers
            break
    return None

print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,4]))
# print(howSum(300, [7,14]))


#? FREECODECAMP SOLUTION FOR BRUTE FORCE

def howSum2(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult is not None:
            remainderResult.append(num)
            return remainderResult
    return None

print(howSum2(7, [5,3,4,7]))
print(howSum2(7, [2,4]))
# print(howSum2(300, [7,14]))

print(howSum(9, [5,3,4,6,9]))
print(howSum2(9, [5,3,4,6,9]))
