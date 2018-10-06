'''
Created on Jul 4, 2018

@author: Mussie Habtemichael
'''

# Sets up the steps function with a memo
def getSteps(n):
    memo = [None] * (n + 1) # extra space for easier indexing
    return steps(n, memo)

# Finds the total number of steps in the stair problem
def steps(n, memo):
    if n == 0 or n == 1:
        return n
    elif n == 2:
        if memo[n] == None:
            memo[n] = steps(n-1, memo) + 1
        return memo[n]
    elif n >= 3:
        if memo[n] == None:
            memo[n] = steps(n-1, memo) + steps(n-2, memo) + 1
        return memo[n]

def main():
    print(getSteps(4))

if __name__ == "__main__":
    main()