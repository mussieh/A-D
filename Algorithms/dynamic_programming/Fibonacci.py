'''
Created on Feb 8, 2018
@author: Mussie Habtemichael
'''
# Function that implements a top-down dynamic programming
# algorithm for calculating the nth Fibonacci value
def fibonacci(n, myTable):
    if n == 0 or n == 1:
        return n

    if myTable.get(n, None) == None:
        myTable[n] = fibonacci(n-1, myTable) + fibonacci(n-2, myTable)
    
    return myTable[n]

# Function that implements a bottom-up dynamic programming
# algorithm for calculating the nth Fibonacci value
def fiboIter(n):
    if n == 0 or n == 1: return n
    memo = [None] * n
    memo[0] = 0
    memo[1] = 1
    
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n-1] + memo[n-2]

# main function
def main():
    n = 100 # test value
    topDownHashTable = {} # search table declaration
    print("Fibonacci Number is ", fibonacci(n, topDownHashTable))
    print("Fibonacci Number is ", fiboIter(n))

if __name__=="__main__":
    main()