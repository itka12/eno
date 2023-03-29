# # exercise 4


# size(600, 600)
# strokeWeight(5)

# stroke(255, 255, 0)
# line(100, 0, 100, 600)
# line(200, 0, 200, 600)
# line(300, 0, 300, 600)
# line(400, 0, 400, 600)
# line(500, 0, 500, 600)


# stroke(255, 0, 0)
# x = 105
# while(x < 600):
    
#     line(x, 0, x, 600)
#     x += 100
    
    
#  #horizontal line
# stroke(0, 255, 255) #horizontal line
# b = 105
# while b < 600:
#     line(0, b, 600, b)
#     b += 100
    
    
# stroke(0, 0, 255)    
# a = 10
# m = 10
# while a < 600:
#     line(a, m, 600, 600)
#     a += 100


# #exercise 5

# size(500, 500)

# fill(128)
# x = 0
# while x < width:
#     fill(x / 2)
#     rect(x, 0, 100, 100)
#     x += 100

# b = 50
# while b < width:
#     fill(255 - b / 2)
#     ellipse(b, 250, 100, 100)
#     b += 100
    
# #mission 

# size(600, 600)
# x = 0
# r = 255
# g = 255
# b = 255
# fill(r, g, b)
# while x < width:
#     fill(r - x/2, g - x/2, b)
#     rect(x, 0, 100, 100)
#     x += 100



#exercise 6 mission

# size(600, 600)
# i = 0 
# while i < 50:
#     s = random(50)
#     l = random(50)
#     r = random(255)
#     g = random(255)
#     b = random(255)
#     fill(r, g, b)
#     ellipse(random(width), random(height), s, l)
#     i += 1


#exercise 7 
ps = 2
def setup():
    size(600, 600)
    noStroke()
    # stroke(255, 255, 0)
    # strokeWeight(ps)
    
def draw():
    i = 0
    while i < 1:
        s = random(50)
        l = random(50)
        r = random(200, 255)
        g = random(200, 255)
        b = random(200, 255)
        o = random(255)
        fill(r, g, b, o)
        ellipse(random(width), random(height), s, l)
        i += 1
    
    # i = 0
    # while i < 1:
    #     x = random(width)
    #     y = random(height)
    #     point(x, y)
    #     i += 1
