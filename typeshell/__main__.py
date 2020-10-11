import sys
import argparse
from random import choice
from time import perf_counter
import pytype as pt

def main():
	parser = argparse.ArgumentParser(description='Practice your typing speed.')
	parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
	parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')
	parser.add_argument('-c', '--create', type=int, help='create a typing session')
	args = parser.parse_args()


	
	

	if args.create:
		begin_test(args.create)

def begin_test(n):
	with open('/Users/greysonmurray/Desktop/prompts.txt','r') as f:
			prompts = list(f)
			for i in range(n):
				prompt = choice(prompts)
				print(prompt)
				start = perf_counter()
				user_input = input()
				finish = perf_counter()
				print(f'You took {str(finish-start)} seconds to type this prompt.')


if __name__ == '__main__':
	main()