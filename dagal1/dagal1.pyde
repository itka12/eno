def setup():
    size(600, 600)

def draw():
    ellipse1()
    ellipse2()
    ellipse3()
    
def ellipse1():
    
    ell1 = color(255, 0, 0)
    fill(ell1)
    ellipse(100, 100, 100, 100)
    if mouseX < 150:
        if mouseY < 150:
            if mouseX > 50:
                if mouseY > 50: 
                    ell1 = color(255, 255, 255)
                    fill(ell1)
                    ellipse(100, 100, 100, 100)
                    
def ellipse2():
    ell2 = color(255, 255, 0)
    fill(ell2)
    ellipse(300, 500, 100, 100)
    if mouseX > 250:
        if mouseY > 450:
            if mouseX < 350:
                if mouseY < 550: 
                    ell2 = color(255, 255, 255)
                    fill(ell2)
                    ellipse(300, 500, 100, 100)
                    
def ellipse3():
    ell3 = color(0, 0, 255)
    fill(ell3)
    ellipse(500, 100, 100, 100)
    if mouseX > 450:
        if mouseY <150:
            if mouseX < 550:
                if mouseY > 150:
                    ell3 = color(255, 255, 255)
                    fill(ell3)
                    ellipse(500, 100, 100, 100)
