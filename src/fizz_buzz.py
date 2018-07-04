'''
Created on Feb 14, 2018

@author: Mussie
'''

# The FizzBuzz method
def fizzBuzz(start, end):
    modThreeStatus = 0
    modFiveStatus = 0
    
    # Test range from start to end
    for num in range(start,end):
        modThreeStatus = num % 3
        modFiveStatus = num % 5
        if modThreeStatus == 0 and modFiveStatus != 0:
            print("Fizz: " + str(num))
        if modFiveStatus == 0 and modThreeStatus != 0:
            print("Buzz: " + str(num))
        if modThreeStatus == 0 and modFiveStatus == 0:
            print("Fizz Buzz: " + str(num))
        
# main function
def main():
    start = 1
    end = 101
    fizzBuzz(start, end)

if __name__=="__main__":
    main()