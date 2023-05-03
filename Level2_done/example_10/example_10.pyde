scores = [89, 100, 90, 80, 78]

# built-in function max() and sum()
print("Sum by built-in function sum", sum(scores))
print("Max by built-in function max", max(scores))
print("Min by built-in function min", min(scores))

# built-in functions
# https://docs.python.org/3/library/functions.html

# calc sum and average with built-in functions
total_sum = 0
for s in scores:
    total_sum += s
  
print("Total sum is", total_sum)
print("Average is", total_sum / len(scores))

# find max
current_max = scores[0]
for s in scores:
    if s > current_max:
        current_max = s
print("Max is", current_max)










#
