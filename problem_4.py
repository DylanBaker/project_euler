"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math import floor


def is_palindrome(product):
	product = str(product)
	if len(product) == 1:
		return True
	else:
		for i in range(0,floor(len(product)/2)):
			if product[i] != product[len(product)-(i+1)]:
				return False
		return True


def problem():
	three_digit_numbers = range(100,1000)
	max = 0
	for i in three_digit_numbers:
		for j in three_digit_numbers:
			if is_palindrome(i*j) and i*j > max:
				max = i*j
	return max


if __name__ == "__main__":
	print(problem())
