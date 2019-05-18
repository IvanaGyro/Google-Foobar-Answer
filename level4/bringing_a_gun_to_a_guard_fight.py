'''
Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! 
Fortunately, you grabbed a beam weapon from an abandoned guard post while you 
were running through the station, so you have a chance to fight your way out. 
But the beam weapon is potentially dangerous to you as well as to the elite 
guard: its beams reflect off walls, meaning you'll have to be very careful where 
you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming 
too weak to cause damage. You also know that if a beam hits a corner, it will 
bounce back in exactly the same direction. And of course, if the beam hits 
either you or the guard, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, guard_position, distance) 
that gives an array of 2 integers of the width and height of the room, an array 
of 2 integers of your x and y coordinates in the room, an array of 2 integers of 
the guard's x and y coordinates in the room, and returns an integer of the 
number of distinct directions that you can fire to hit the elite guard, given 
the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and 
the elite guard are both positioned on the integer lattice at different distinct 
positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. 
Finally, the maximum distance that the beam can travel before becoming harmless 
will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with 
dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum 
shot distance of 4, you could shoot in seven different directions to hit the 
elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, 
-2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at 
bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at 
bearing [-3, -2] bounces off the left wall and then the bottom wall before 
hitting the elite guard with a total shot distance of sqrt(13), and the shot at 
bearing [1, 2] bounces off just the top wall before hitting the elite guard with 
a total shot distance of sqrt(5).

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
Solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9

-- Python cases --
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9

Use verify [file] to test your solution and see how it does. When you are 
finished editing your code, use submit [file] to submit your answer. If your 
solution passes the test cases, it will be removed from your home folder.
'''
from fractions import gcd
def solution(dimensions, your_position, guard_position, distance):
    x, y = your_position
    xm_o, ym_o = x, y
    xg_o, yg_o = guard_position
    x_dim, y_dim = dimensions
    to_self = set()
    res = set()

    def shoot(x_off, y_off):
        if x_off % 2 == 0:
            xm = x_off * x_dim + xm_o
            xg = x_off * x_dim + xg_o
        else:
            xm = (x_off + 1) * x_dim - xm_o
            xg = (x_off + 1) * x_dim - xg_o
        if y_off % 2 == 0:
            ym = y_off * y_dim + ym_o
            yg = y_off * y_dim + yg_o
        else:
            ym = (y_off + 1) * y_dim - ym_o
            yg = (y_off + 1) * y_dim - yg_o
        dxm_o, dym_o = xm - x, ym - y
        dxg_o, dyg_o = xg - x, yg - y
        if dxg_o**2 + dyg_o**2 > distance**2:
            return False
        g = gcd(abs(dxm_o), abs(dym_o)) or 1
        dxm, dym = dxm_o // g, dym_o // g
        g = gcd(abs(dxg_o), abs(dyg_o)) or 1
        dxg, dyg = dxg_o // g, dyg_o // g
        if (dxg, dyg) not in to_self:
            if (dxg, dyg) != (dxm, dym) or \
                dxm_o**2 + dym_o**2 > dxg_o**2 + dyg_o**2:
                res.add((dxg, dyg))
        to_self.add((dxm, dym))
        return True

    x_off = 0
    flag = False
    while True:
        y_off = 0
        cnt = 0
        while shoot(x_off, y_off):
            cnt += 1
            y_off += 1
        y_off = -1
        while shoot(x_off, y_off):
            y_off -= 1
            cnt += 1
        if cnt == 0:
            if flag:
                break
            flag = True
            x_off = 0
        x_off += 1 if not flag else -1
    
    return len(res)
