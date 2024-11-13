def knapSack(W, wt, val): 
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif wt[i-1] <= j: 
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]], table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][W] 

# User input
n = int(input("Enter the number of items: "))
val = list(map(int, input("Enter values of items separated by space: ").split()))
wt = list(map(int, input("Enter weights of items separated by space: ").split()))
W = int(input("Enter maximum weight capacity of knapsack: "))

# Ensure the user provided correct input
if len(val) != n or len(wt) != n:
    print("Error: The number of values and weights must match the number of items.")
else:
    max_value = knapSack(W, wt, val)
    print("Maximum value in knapsack =", max_value)
