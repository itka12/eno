# level 2:
#     example 9

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)

# print(numbers[5])

# for i in numbers:
#     if i < 11:
#         print(i)
# #example 9 

# def setup():
#     size(600, 600)
#     frameRate(2)
    
#     noStroke()
    
# def draw():
#     c = color(random(100, 255), random(100, 255), random(100, 255), random(50, 100))
#     background(c)

#     i = 0
#     while i < 90:
        
#         bxy = random(50, 100)

#         fill(random(150, 255), random(150, 255), random(150, 255), random(100, 255))
#         ellipse(random(width), random(height), bxy, bxy)
#         i += 1


#example 10

numbers = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total_sum = 0
for i in numbers:
    total_sum += i
print("total sum is", total_sum)
print("total sum is ", sum(numbers))
print("total max is", max(numbers))

print("in a number list ", len(numbers))
print('average is ', sum(numbers) / len(numbers))
