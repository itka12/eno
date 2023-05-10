def setup():
    drawtree_JunhanPark(100, 100, color(255, 255, 0), color(0, 255, 0), color(225, 127, 0), 200, 200)
    size(600, 600)
    
    
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

    
def draw():
    drawtree_JunhanPark(100, 100, color(255, 0, 0), color(0, 255, 255), color(0, 0, 255), 200, 200)
    
    
def drawtree_JunhanPark(x, y, r, g, b, sizeX, sizeY):
    
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
    
