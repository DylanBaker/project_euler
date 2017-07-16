
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import ceil, sqrt


def is_prime(number):
	upper_limit = ceil(sqrt(number))
	for i in range(2,upper_limit):
		if number % i == 0:
			return False
	return True


def problem(number):
	upper_limit = ceil(sqrt(number))
	for i in reversed(range(2,upper_limit)):
		if number % i == 0:
			if is_prime(i):
				return i


if __name__ == "__main__":
	print(problem(600851475143))