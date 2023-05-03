# Let's make your function
# - to draw one of these: Spring, Summer, Fall, Winter, Animals, Trees, Your identity logos/characters, et al.  
# - your name should be in your function name like this: def itemTitle_YourName()
# - canvas size should be 500 * 500 pixels
# - it has to have at least these 2 parameters (x, y) which are left top corner of your works 
# - it also needs DocString in your function definition. 
# - You HAVE TO make your own making film, running time is 1 minute, and upload it on the Internet to share it.

URLs = [
        ["https://drive.google.com/file/d/1W2fXSko6ifJq-3ePjSMMwEcey-ry2yFu/view?usp=sharing",
         "https://drive.google.com/file/d/1W2fXSko6ifJq-3ePjSMMwEcey-ry2yFu/view?usp=sharing"],
        
        ["https://drive.google.com/file/d/1W2fXSko6ifJq-3ePjSMMwEcey-ry2yFu/view?usp=sharing",
        "https://drive.google.com/file/d/1W2fXSko6ifJq-3ePjSMMwEcey-ry2yFu/view?usp=sharing"]
        ]
        

def setup():
    size(1000, 1000)
    
def draw():
    #drawFace_KeechulJung(0*500, 0*500, color(random(255), random(255), random(255)))
    #drawFace_KeechulJung(1*500, 0*500, color(random(255), random(255), random(255)))
    #drawFace_KeechulJung(0*500, 1*500, color(random(255), random(255), random(255)))
    #drawFace_KeechulJung(1*500, 1*500, color(random(255), random(255), random(255)))
        
    for row in range(2):
        for col in range(2):
            drawFace_KeechulJung(col*500, row*500, color(random(255), random(255), random(255)))
             
def drawFace_KeechulJung(x, y, c):
    """ 
    Draws smiling face image
    
    Paramters:
        x (int): start left top x
        y (int): starting left top y
        c (color): color in hexa-decimal(ex. 0xff00ff00 or color() data type)
    Returns:
        None 
    """
    x += 250
    y += 250
    # face
    fill(c) #
    stroke(0)
    strokeWeight(10)
    ellipse(x, y, 200, 200)
    # eyes
    fill(0xff000000)
    ellipse(x-35, y-20, 30, 30)
    ellipse(x+35, y-20, 30, 30)
    fill(0xfffffffa)
    noStroke()
    ellipse(x-40, y-25, 15, 15)
    ellipse(x+30, y-25, 15, 15)  
    # mouth
    noFill()
    stroke(0)
    arc(x, y, 100, 100, 0+0.8, PI-0.8)
    
def mousePressed():
    x = mouseX // 500
    y = mouseY // 500
    link(URLs[y][x])
