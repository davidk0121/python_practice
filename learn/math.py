# Division is decimal by default
print(5 / 2)  # Output: 2.5

# Double slash rounds down
print(5 // 2)  # Output: 2

# negative numbers will still round down
print(-5 // 2)  # Output: -3
# to round towards ZERO, we can use int() instead
print(int(-5/2))  # Output: -2


print(2 ** 3)  # Output: 8
print(10 % 3)  # Output: 1, because 10 = (3 * 3) + 1
print(-10 % 3) # Output: 2, because -10 = (-4 * 3) + 2
# to be consistenet with other languages modulo
import math
print(math.fmod(-10, 3)) # Output: -1.0, because -10 = (-3 * 3) + (-1)

import math
print(math .floor(3/2)) # Output: 1
print(math.ceil(3/2)) # Output: 2
print(round(3/2)) # Output: 2, rounds to nearest integer, ties go to even numbers
print(math.sqrt(2))
print(math.pow(2,3))

# Max/Min Int
float("inf")
float("-inf")

