import random as rand
import copy

'''
This function, given an input value N, produces a randomized list
with each value from 1 to N. Naively, this can be done by actually
simulating a real shuffle, as I did in a prior assignment, but since
we want to optimize for speed, we're going to have to be more
creative. The first idea that came to mind was to lay out all the
'cards', then randomly pick a card index, then take the card at that
index and put it into my new random shuffle. The problem, here, is 
that removing from an arbitrary index in a Python list is O(n),
so if I do this n times, I get an O(n^2) algorithm, which is no
better than naively shuffling!

Clearly, the problem is with removing. But the trick is, editing entries 
is an O(1) operation! So why don't we just boot it to the end of the list
by exchanging it with whatever was at the end of the list, and then stop
considering that end of the list?
'''

'''
Card index 'removal' shuffle. Since removal is costly, but editing the values of the list aren't, the current idea is to boot the chosen element to the 'end of the list' by exchanging it with the value at the end of the list, then decrement the 'size of the list' counter.

Algorithm should be an O(N) algorithm, where N is length of the input list.

Parameters:
	inputList: An input list of any sort of item.
Returns:
	outputList: A new list containing the elements of the input list, shuffled.
	
Maybe Improve:
	random.randint is known to be relatively costly; if there's a way to substitute out the random index generating function for
	something else, we can gain additional speed. Marginal improvement compared to simply getting a good algorithm.
'''
def listShuffle(inputList):
	outputList = []

	listSize = len(inputList)
	workingList = copy.deepcopy(inputList)
	lastPos = listSize-1
	
	for iteration in range(listSize):
		#get a candidate position in the list
		candidate = rand.randint(0, lastPos) #getRandInt(lastPos)
		
		#attach it to the output list
		outputList.append(workingList[candidate])
		
		#exchange candidate with last entry in list.
		temp = workingList[lastPos]
		workingList[lastPos] = workingList[candidate]
		workingList[candidate] = temp
		
		#Increase the dead zone.
		lastPos -= 1
	
	return outputList

'''
Given an integet input N, generates a list of numbers
from 1 to N, shuffled and randomized.

Algorithm should be an O(N) algorithm.

Parameters:
	N: The input integer from 1 to N.
Returns:
	List of integers from 1 to N, shuffled.
'''
def randList(N):
  numList = []
  #Generate list of numbers from 1 to N. O(N) step.
  for val in range(1, N+1):
    numList.append(val)
  #Shuffle the list.
  return listShuffle(numList) #O(N) step.

#Program proper.
print("Input an integer number N")
list = randList(int(input()))
print(list)
#Hit enter to leave.
print("Hit enter to leave.")
input()