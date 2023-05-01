#head x, y
x = 250
y = 250
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
    
    # head 
    fill(head)
    ellipse(x, y, 400, 400)
    
    #faceWhite
    fill(face)
    ellipse(255, 300, 285, 280)
    
    #mount
    fill(mount)
    noFill()
    arc(255, 310, 200, 180, 0, PI, OPEN)
    
    #eyesRight
    fill(eyes)
    ellipse(305, 180, 100, 150)
    
    #eyesLeft
    fill(eyes)
    ellipse(205, 180, 100, 150)
    
    #nose
    fill(nose)
    circle(255, 230, 50)
    
    #NoseMountline
    line(255, 255, 255, 400)
    
    #innerEyesLeft
    fill(innerEyes)
    ellipse(230, 190, 20, 30)
    fill(innerEyes1)
    ellipse(232, 192, 9, 9)
    
    #innerEyesRight
    fill(innerEyes)
    ellipse(280, 190, 20, 30)
    fill(innerEyes1)
    ellipse(280, 190, 9, 9)
    
    #LeftmMustage
    stroke(0);
    line(60, 260, 185, 270)
    stroke(0);
    line(60, 280, 185, 280)
    stroke(0);
    line(60, 300, 185, 290)
    
    #RightMustage
    stroke(0);
    line(315, 270, 440, 260)
    stroke(0);
    line(315, 280, 440, 280)
    stroke(0);
    line(315, 290, 440, 300)


    
    
