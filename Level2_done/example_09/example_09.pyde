# for loop with list data type
# list data type: we will cover this later in detail.
# for now, let's see the intro...

# without list
animal0 = "dog"
animal1 = "cat"
animal2 = "bird"

print(animal0)
print(animal1)
print(animal2)

# with list
animals = ["dog", "cat", "bird"]

# indexing
print(animals[0])
print(animals[1])

# index out of range ERROR
print(animals[3])

# list with loop statment
i = 0
while i < 3:
    print(animals[i])
    i += 1

animals = ["dog", "cat", "bird"]

# for loop
for animal in animals:
    print(animal)
    
for a in animals:
    print(a)
    
numbers = [1, 2, 3, 100, 20, 123]
print(numbers)
print(numbers[4])
    
for n in numbers:
    if n > 100:
        print(n, "score is larger than 100")
    else:
        print(n)
    
    
    
    
    
    
#
