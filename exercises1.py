# 1.12 EXERCISES 

# R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n, m):
  return not bool(n%m)

# R-1.2 Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
  return not bool (k%2)

# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
  min, max = data[0], data[0]

  for number in data:
    if number < min:
      min = number

    if number > max:
      max = number

  return min, max

# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sqsum(n):
  sum = 0
  for i in range(n):
    sum += i*i
  
  return sum

