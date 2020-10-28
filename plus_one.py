'''
Given:
  An array of non-negative digits that represent a decimal integer.

Problem:
  Add one to the integer. Assume the solution still works even if 
  implemented in a language with finite-precision arithmetic.
'''


def plus_one(A: [int]) -> [int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    # Check the first digit
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A


A1 = [1, 4, 9]
A2 = [9, 9, 9]
print(plus_one(A1), plus_one(A2))
