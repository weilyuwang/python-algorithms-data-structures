"""
you are given an array of non - negative integers. For example:

[3, 3, 1, 0, 2, 0, 1].

Each number represents the maximum you can advance in the array.

Question:
Is it possible to advance from the start of the array to the last element?
"""


"""
Approach

- Iterate through each entry in the arry
- Track furthest we can reach from entry (i + A[i])
- If for some "i" before the end is the furthest we can reach,
  we can't reach the last index. Otherwise, the end is reached.

- i: index processed
- Furthest possible to advance from "i": i + A[i]
"""


def array_advance(A: [int]) -> bool:
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached:
        furthest_reached = max(furthest_reached, A[i] + i)

        if furthest_reached >= last_idx:
            return True

        # Keep moving
        i += 1

    # i > furthest_reached => can't reach to the end
    return False


A1 = [3, 3, 1, 0, 2, 0, 1]
A2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A1), array_advance(A2))  # Should see True, False
