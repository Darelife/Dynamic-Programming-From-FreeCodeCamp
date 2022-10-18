# m = rows, n = columns
# How many ways can you go from top left to bottom right?
# You can only go down or right
# Grid (x,y)

def grid_traveller(m, n):
    if m==1 and n==1: return 1
    elif m==0 or n==0: return 0
    elif m==1 and n!=1: return n
    elif m!=1 and n==1: return m
    return grid_traveller(m-1, n) + grid_traveller(m, n-1)

# print(grid_traveller(10,3))
# print(grid_traveller(18,18)) # won't load cuz it's too slow