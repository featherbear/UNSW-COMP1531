'''
Write a program that, given the index, will calculate the n-th number in the 
Fibonacci sequence. The Fibonacci sequence is defined as :

f(x) = 
	| x == 0     = 0
	| x == 1     = 1
	| otherwise  = f(x - 1) + f(x - 2)

The index is to be read from the standard input and the Fibonacci number at 
that index is to be printed to the standard output. You may assume that your
program will be tested with valid inputs only.
'''

# HINT: keep extending this dict with more numbers of the sequence
# HINT: you must make use of this dict to be able to handle large inputs!
fib_dict = {
	0: 0,
	1: 1,
	2: 1,
	3: 2
}

# Define this function to return the expected output
# Do not print it from this function
def fib_sequence(num):
	
	# TODO fill in this part

	return fib_dict[num]


if __name__ == '__main__':
	number = int(input("Enter the number:\n"))
	print(f'The number in position {number} is: ')
	print(fib_sequence(number))
 