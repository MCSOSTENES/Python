"""
There's a wolf who lives in the plane forest, which is located on the Cartesian coordinate system. When going on the hunt, the wolf starts at point (0, 0) and goes spirally as shown in the picture below:

https://www.codewars.com/kata/591c075a94414c1617000063/train/python

The wolf finally found something to eat at point (x, y). Your task is to calculate the number of turns he had to make to get to that point.

Input/Output
[input] integer x

x coordinate of the final point.

-1000000 ≤ x ≤ 1000000

[input] integer y

y coordinate of the final point.

-1000000 ≤ y ≤ 1000000

[output] an integer

The number of turns.

Example
For x = 1 and y = 1, the output should be 1.

Path:(0,0) --> (0,1) --> (1,1), 1 turn at (0,1)

For x = 1 and y = -1, the output should be 4.

Path:(0,0) --> (0,1) --> (1,1) --> (-1,1) --> (-1,-1) --> (1,-1),

4 turns at (0,1), (1,1), (-1,1), (-1,-1)

"""
# minha solucao (reescrita)
def turns_on_road(x, y):
    if y == 0: return 0                             #First line y = 0
    if x > 0 and -x + 1 < y <= x: return 4*x -3     #vertical line x positive
    if y > 0 and -y <= x < y: return 4*y -2         #horizontal line y positive
    if x < 0 and x <= y < -x: return 4*(-x) -1      #vertical line x negative
    if y < 0 and y < x <= -y + 1: return 4*(-y)     #horizontal line y negative
    

print(turns_on_road(-2,1))       #,7) 
print(turns_on_road(1,-1))       #,4) 
print(turns_on_road(1,0))       #,0) 
print(turns_on_road(-1,-1))       #,3) 
print(turns_on_road(10,10))       #,37) 
print(turns_on_road(0,0))       #,0) 
print(turns_on_road(2,-1))       #,4) 
print(turns_on_road(2,2))       #,5) 
print(turns_on_road(3,5))       #,18)
print(turns_on_road(11168, -91457))       #,365828)
print(turns_on_road(875286,925200))       #,3700798)
print(turns_on_road(1000000,1000000))       #,3999997)