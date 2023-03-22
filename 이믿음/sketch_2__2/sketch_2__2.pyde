x = 0 # ball's x position
i = 0
b = 0
n = 255
m = 0
def setup():
  size(800, 600)
  global x
  x = 0
  fill(255, 0, 0)
  

def draw():
  background(255,  0, 0)
  global x
  global i
  global b
  global n
  global m
  fill(n, b, i)
  ellipse(x, m, 50, 50)
  x = x + 1
  i = i + 1
  b = b + 1
  if b > 254:
      b = b - 1
  elif b < 1:
      b = b + 1
  n = n - 1
  if n < 1:
      n = n + 1
  elif n > 254:
      n = n + 1
  m = m + 1
