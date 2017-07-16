"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors


def problem(upper_limit):
	answer = 1
	for i in reversed(range(1,upper_limit+1)):
		answer_temp = answer
		for j in prime_factors(i):
			if answer_temp % j == 0:
				answer_temp //= j
			else:
				answer *= j
	return answer


if __name__ == "__main__":
	print(problem(20))
