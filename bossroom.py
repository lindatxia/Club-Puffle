import time 

#1, Project Euler 
def multiples(): 
	sum = 0 
	# Find the sum of all the multiples of 3 or 5 below 1000.
	for x in range(1000): 
		if x%3 == 0 or x%5 == 0: 
			sum += x 
	return sum 
print(multiples())

#2, Project Euler -- Memoized fib 
fibDict = dict() 
def fib(n): 
	if n in fibDict: 
		 result = fibDict[n]
	if n < 2: 
		return 1 
	else: 
		result = fib(n-1) + fib(n-2)
	return result
print(fib(3), "memoized")

def findEvenFibSum(): 
	sum = 0 
	for x in range (10):
		if fib(x) % 2 == 0: 
			sum += fib(x) 
	return sum

print(findEvenFibSum(),"even sum")










# The string way 
class Solution(object):
	def reverse(self, x):
		x = str(x) 
		x = x[::-1]
		return (int(x))
runThis = Solution() 
print(runThis.reverse(123))


# The 100% integer way 
class Solution(object): 
	def reverse(self,x): 
		digCount = 0 
		temp = 0 
		newDig = 0 
		counter = 0
		orig = x 
		while(x > 0): #digit count 
			digCount += 1 
			x//=10 
		x = orig 
		while(x > 0): 
			temp = x%10 
			newDig += temp*(10**(digCount-counter-1))
			counter += 1
			x//=10
		return newDig

otherThis = Solution() 
print(otherThis.reverse(123))

