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

def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = bestSum(remainder, numbers, memo)
        if remainderResult is not None:
            remainderResult = remainderResult + [num] #We use + instead of append because we 
            # want to make our list of numbers and not a list of lists
            # append -> remainderlist.append(num) -> [remainderListElement, [num]] #we don't want 'num'
            # as a list inside a list
            # + -> remainderlist + [num] -> [remainderListElement, num]
            if shortestCombination is None or len(shortestCombination)>len(remainderResult):
                shortestCombination = remainderResult
    memo[targetSum] = shortestCombination
    return memo[targetSum] #return is outside loop cuz we need to make sure that it's the shortest 
    #combination that we return and not just the first combination that we find

print(bestSum(7, [5,3,4,9]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))
print(bestSum(300, [7,14]))
