from turtle import *

color('green', 'blue')
begin_fill()
while True:
    fd(220)
    lt(192)
    rt(82)
    if abs(pos()) < 1:
        break

end_fill()
done()
