'''
Created on Feb 9, 2018
@author: Mussie Habtemichael
'''

# Method to find the Powerset
def getPowerSet(givenList):
    currentList = [[]]
    for i in range(0, len(givenList)):
        for j in range(len(currentList)):
            currentList.append(currentList[j] + [givenList[i]])        
    return currentList

def main():
    testList = [1,2,3]
    print(getPowerSet(testList))

if __name__=="__main__":
    main()