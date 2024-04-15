"""
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num%2 == 0]
print(result)
"""


"""
result = [x * y for x in range(2 ,10)
          for y in range(1, 10)]
print(result)
"""


words = ["apple", "banana", "blueberry", "orange"]
word_lengths = [len(i) for i in words ]
word_lengths
[5, 6, 9, 6]
