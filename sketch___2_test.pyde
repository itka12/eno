URLs = [
        ["https://www.youtube.com/watch?v=B6QmielXysE",
         "https://www.youtube.com/watch?v=WXpj3Ij8D38"],
        
        ["https://drive.google.com/file/d/1jC3ljVQclZ6StuR0mFuthtLiquWwPyAy/view?usp=sharing",
         "https://www.youtube.com/watch?v=WXpj3Ij8D38"]
        ]

def setup():
    size(1000, 1000)
    
def draw():

    #frog_Jeonghwan
    #draw_dog_kim
    #drawFace_KeechulJung(0*500, 1*500, color(random(255), random(255), random(255)))
    #drawFace_KeechulJung(1*500, 1*500, color(random(255), random(255), random(255)))

    frog_Jeonghwan(0, 0, color(0, 255, 0), color(0), color(255, 0, 0))
    draw_dog_kim(700, 230)
    drawSun_Parkjaeyeon(250, 700, 200, 80, 130)


def drawSun_Parkjaeyeon(x, y, maximumLength=200, randomness=80, numOfRays=130):

    # Draws a sunburst pattern with rays emanating from a point at (x,y).

    # Parameters:
    #     x (int): The x coordinate of the center point of the sunburst.
    #     y (int): The y coordinate of the center point of the sunburst.
    #     maximumLength (int, optional): The maximum length of the rays. Default is 200.
    #     randomness (int, optional): The amount of randomness in the length of the rays. Default is 80.
    #     numOfRays (int, optional): The number of rays in the sunburst. Default is 130.

    # Returns:
    #     None

    pushStyle()
    fill(255, 246, 64)
    stroke(255, 246, 64)
    strokeWeight(5)
    radius = 0
    angle = TWO_PI / float(numOfRays)

    for i in range(numOfRays):
        radius = maximumLength - int(random(0, randomness))
        line(x, y, radius * sin(angle * i) + x, radius * cos(angle * i) + y)

    stroke(51)
    strokeWeight(4)
    arc(x-50, y, 40, 30, PI, TWO_PI)
    arc(x+50, y, 40, 30, PI, TWO_PI)
    arc(x, y+35, 100, 70, PI / 6, 5 * PI / 6)
    popStyle()
def drawtree_JunhanPark(x, y, r, g, b, sizeX, sizeY):
    

    # Draws tree image
    
    # Paramters
    # x(int): left top x(control point is trunk, not leaves or branches)
    # y(int): left top y(control point is trunk, not leaves or branches)
    # r(int): leaves color (red)
    # g(int): leaves color (green)
    # b(int): leaves color (blue)
    # you can use this to change leaves color for your own theme
    # (ex. 255, 255, 0 is yellow / 0, 255, 0 is green / 225, 127, 0 is orange / 220, 20, 60 is maple)
    # if you use only the trunk and branches, make the 'r' value above 256
    # sizeX(int): trunk length x
    # sizeY(int): trunk length y
    # branches and leaves are adjusted to fit trunk size
    
    a = color(150, 75, 0)
    b = color(r, g, b)
    
    noStroke()
    
    trunk = createShape(RECT, x, y, sizeX, sizeY)
    trunk.setFill(a)

    leaves = createShape(ELLIPSE, x + sizeX / 2, y - sizeY / 8, sizeX * 65 / 30, sizeX * 65 / 30)
    leaves.setFill(b)
    
    branch1 = createShape(TRIANGLE, x, y, x - sizeX / 3, y - sizeY / 4, x + sizeX / 3, y)
    branch1.setFill(a)
    
    branch2 = createShape(TRIANGLE, x + sizeX, y, x + sizeX + sizeX / 3, y - sizeY / 4, x + sizeX - sizeX / 3, y)
    branch2.setFill(a)


    if r < 255:
        shape(leaves)
        
    shape(trunk)
    shape(branch1)
    shape(branch2)


    stroke(0)
def draw_dog_kim(x, y, rotation=0):
    # Draw a dog for given position and rotation.
    
    # Args:
    #     x(int): top-left position of a dog in x direction in pixel.
    #     y(int): top-left position of a dog in y direction in pixel.
    #     rotation(int): optional parameter, rotation of a dog in radian.
        
    # Returns:
    #     None

    x_margin = 50
    y_margin = 40
    translate(x + x_margin, y + y_margin)
    rotate(rotation)
    
    # draw ears
    fill(230,200,150)
    rotate(PI/6)
    ellipse(-33, 10, 30, 40)
    rotate(-PI/6)
    
    rotate(-PI/6)
    ellipse(33, 10, 30, 40)
    rotate(PI/6)
    
    # draw a face
    ellipse(0, 0, 65, 75)
    
    # draw eyes
    fill(0,0,0)
    ellipse(-13, -10, 15, 15)
    ellipse(+13, -10, 15, 15)
    fill(255,255,255)
    ellipse(-16, -13, 9, 9)
    ellipse(+10, -13, 9, 9)
    
    # draw a nose
    fill(210,170,120)
    ellipse(0, +10, 15, 10)
    
    # draw a mouth
    fill(230,50,50)
    ellipse(0, 0+30, 15, 5)
    
    # reset the configuration
    fill(255)
    rotate(-rotation)
    translate(-x-x_margin, -y-y_margin)
    

def frog_Jeonghwan(x, y, c1, c2, c3):
    '''
    Draw frog image
    
    Paraments:
        x (int) : start left top x
        y (int) : starting left top y
        c1 (color) : the color of frog's face
        c2 (color) : the color of frog's eyes
        c3 (color) : the color of frog's mouth
    Retruns:
        None
    '''
    x += 250
    y += 250
    noStroke()
    #face
    fill(c1)
    ellipse(x, y, 300, 200)

    ellipse(x - 70, y - 100, 80, 80)
    ellipse(x + 60, y - 100, 80, 80)

    #eyes
    fill(c2)
    ellipse(x - 70, y - 100, 30, 30)
    ellipse(x + 60, y - 100, 30, 30)

    #mouth
    fill(c3)
    arc(x, y, 150, 100, 0.1* PI, 0.9*PI, OPEN)
    

    
def mousePressed():
    x = mouseX // 500
    y = mouseY // 500
    link(URLs[y][x])
