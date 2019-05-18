'''
Dodge the Lasers!
=================

Oh no! You've managed to escape Commander Lambdas collapsing space station in 
an escape pod with the rescued bunny prisoners - but Commander Lambda isnt 
about to let you get away that easily. She's sent her elite fighter pilot 
squadron after you - and they've opened fire!

Fortunately, you know something important about the ships trying to shoot you 
down. Back when you were still Commander Lambdas assistant, she asked you to 
help program the aiming mechanisms for the starfighters. They undergo rigorous 
testing procedures, but you were still able to slip in a subtle bug. The 
software works as a time step simulation: if it is tracking a target that is 
accelerating away at 45 degrees, the software will consider the targets 
acceleration to be equal to the square root of 2, adding the calculated result 
to the targets end velocity at each timestep. However, thanks to your bug, 
instead of storing the result with proper precision, it will be truncated to an 
integer before adding the new velocity to your current position.  This means 
that instead of having your correct position, the targeting software will 
erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough 
off to fail Commander Lambdas testing, but enough that it might just save your 
life.

If you can quickly calculate the target of the starfighters' laser beams to 
know how far off they'll be, you can trick them into shooting an asteroid, 
releasing dust, and concealing the rest of your escape.  Write a function 
solution(str_n) which, given the string representation of an integer n, returns 
the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a 
string. That is, for every number i in the range 1 to n, it adds up all of the 
integer portions of i*sqrt(2).

For example, if str_n was "5", the solution would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can 
be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. 
Sometimes, it's easier to take a step back and concentrate not on what you have 
in front of you, but on what you don't.

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
Solution.solution('77')
Output:
    4208

Input:
Solution.solution('5')
Output:
    19

-- Python cases --
Input:
solution.solution('77')
Output:
    4208

Input:
solution.solution('5')
Output:
    19

Use verify [file] to test your solution and see how it does. When you are 
finished editing your code, use submit [file] to submit your answer. If your 
solution passes the test cases, it will be removed from your home folder.
'''

'''
Refer to https://surajshetiya.github.io/Google-foobar/#round-5
for the explanation.
'''
from bisect import bisect
def sqrt_p10(n, digit):
    if digit <= 0:
        return 0

    def s(root, p, r):
        root *= 10
        p *= 10
        b = r // p
        m = (p + b) * b
        if m > r:
            b -= 1
            m = (p + b) * b
        return root + b, p + (b << 1), r - m

    tmp = int(n)
    if tmp:
        base = 99
        stack = [tmp % 100]
        while base < tmp:
            tmp /= 100
            stack.append(tmp % 100)
        tmp = stack.pop()
        tb = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        root = bisect(tb, tmp) - 1
        tmp -= root ** 2
        p = root << 1
        digit -= 1
        while stack and digit:
            tmp *= 100
            tmp += stack.pop()
            root, p, tmp = s(root, p, tmp)
            digit -= 1
    while digit:
        tmp *= 100
        n *= 100
        tmp += int(n) % 100
        root, p, tmp = s(root, p, tmp)
        digit -= 1
    return root

amplify = 101
sqrt2 = sqrt_p10(2, amplify + 1) - 10 ** amplify

def sum_floor(n):
    if not n:
        return 0
    m = n * sqrt2 / (10 ** amplify)
    return (m + n + 1) * (m + n) / 2 - (m + 1) * m - sum_floor(m)

def solution(s):
    return str(sum_floor(int(s)))
