# Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of
# numbers as arguments.
#
# The function should return an array containing the shortest combination of numbers that
# add up to exactly the targetSum.
#
# If there is a tie for the shortest combination, you may return any one of the shortest.
#
# example : bestSum(7, [5,3,4,7]) -> [7]
#           7 = 7
#
#           bestSum(8, [2,3,5]) -> [3,5]
#           3+5 = 8
#
#           bestSum(8, [1,4,5]) -> [4,4]
#           4+4 = 8
#
#           bestSum(100, [1,2,5,25]) -> [25,25,25,25]
#           25+25+25+25 = 100
#
#           bestSum(8, [1,4,5]) -> None
#           no combination of 1,4,5 can add up to 8
#

#? MY SOLUTION

#* Attempt 1

# def bestSum(targetSum, numbers):
#     if targetSum == 0: return []
#     if targetSum < 0: return None
#     answers = []
#     ans = []
#     for num in numbers:
#         remainder = targetSum - num
#         if bestSum(remainder, numbers) is not None:
#             answers.append(num)
#             ans.append(answers)
#             answers = []
#     if ans != [] or ans != None:
#         ans.sort(key=len)
#         print(ans)
#         return ans[0]
#     return None

# print(bestSum(7, [5,3,4,7]))
# print(bestSum(8, [2,3,5]))

#* After watching the video

def bestSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = bestSum(remainder, numbers)
        if remainderResult is not None:
            remainderResult.append(num)
            if shortestCombination is None or len(shortestCombination)>len(remainderResult):
                shortestCombination = remainderResult

    return shortestCombination #return is outside loop cuz we need to make sure that it's the shortest 
    #combination that we return and not just the first combination that we find

print(bestSum(7, [5,3,4,9]))



#? FREECODECAMP SOLUTION FOR BRUTE FORCE

def bestSum2(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = bestSum2(remainder, numbers)
        if remainderResult is not None:
            combination = remainderResult + [num]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination
    return shortestCombination

print(bestSum2(7, [5,3,4,7]))
