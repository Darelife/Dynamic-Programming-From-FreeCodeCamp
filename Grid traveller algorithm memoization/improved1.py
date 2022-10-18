# m = rows, n = columns
# How many ways can you go from top left to bottom right?
# You can only go down or right
# Grid (x,y)

def grid_traveller(m, n, memo={}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m==1 and n==1: return 1
    elif m==0 or n==0: return 0
    elif m==1 and n!=1: return n
    elif m!=1 and n==1: return m
    memo[key] = grid_traveller(m-1, n, memo) + grid_traveller(m, n-1, memo)
    return memo[key]

print(grid_traveller(10,3))
print(grid_traveller(18,18))