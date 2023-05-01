#head x, y
x = 0
y = 0
#colors 
head = color(36, 99, 255)
face = color(255)
g = color(255)
mount = color(255, 0, 0)
nose = color(255, 0, 0)
eyes = color(255)
innerEyes = color(0)
innerEyes1 = color(255)

def setup():
    size(500, 500)
    

def draw():
    doraemonHead_LeeMidEum(x, y, head, face, mount, nose, innerEyes, innerEyes1)
    
def doraemonHead_LeeMidEum(x, y, head, face, mount, nose, innerEyes, innerEyes1):
    '''
    draws doraemon face image
    parameters: 
        x(int) : left top x
        y(int) : left top y
        head : color in hexa-decimal(ex. 0xff00ff00 or color() data type)
        face : color in hexa-decimal(ex. 0xff00ff00 or color() data type)
        mount : color in hexa-decimal(ex. 0xff00ff00 or color() data type)
        nose : color in hexa-decimal(ex. 0xff00ff00 or color() data type)
        innerEyes : color in hexa-decimal(ex. 0xff00ff00 or color() data type)
        innerEyes1 : color in hexa-decimal(ex. 0xff00ff00 or color() data type)
    returns :
         none
    '''
    # head 
    fill(head)
    ellipse(x + 250, y + 250, 400, 400)
    
    #faceWhite
    fill(face)
    ellipse( X + 255, y +  300, 285, 280)
    
    #mount
    fill(mount)
    noFill()
    arc(x + 255, y + 310, 200, 180, 0, PI, OPEN)
    
    #eyesRight
    fill(eyes)
    ellipse(x + 305, y + 180, 100, 150)
    
    #eyesLeft
    fill(eyes)
    ellipse(x + 205, y + 180, 100, 150)
    
    #nose
    fill(nose)
    circle(x + 255, y + 230, 50)
    
    #NoseMountline
    line(x + 255, y + 255, 255, 400)
    
    #innerEyesLeft
    fill(innerEyes)
    ellipse(x + 230, y + 190, 20, 30)
    fill(innerEyes1)
    ellipse(x + 232, y + 192, 9, 9)
    
    #innerEyesRight
    fill(innerEyes)
    ellipse(x + 280, y + 190, 20, 30)
    fill(innerEyes1)
    ellipse(x + 280, y + 190, 9, 9)
    
    #LeftmMustage
    stroke(0);
    line(x + 60, y + 260, x + 185, y + 270)
    stroke(0);
    line(x  + 60, y + 280, x + 185, y + 280)
    stroke(0);
    line(x + 60, y + 300, x + 185, y + 290)
    
    #RightMustage
    stroke(0);
    line(x + 315, y + 270, x + 440, y + 260)
    stroke(0);
    line(x + 315, y + 280, x + 440, y + 280)
    stroke(0);
    line(x + 315, y + 290, x + 440, y + 300)


    
    
