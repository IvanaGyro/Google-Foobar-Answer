'''
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum anti-
matter fuel injection system for her LAMBCHOP doomsday device. It's a great 
chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit 
of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the 
many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a 
time. However, minions dump pellets in bulk into the fuel intake. You need to 
figure out the most efficient way to sort and shift the pellets down to a 
single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy 
released when a quantum antimatter pellet is cut in half, the safety controls 
will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string 
and returns the minimum number of operations needed to transform the number of 
pellets to 1. The fuel intake control panel can only display a number up to 309 
digits long, so there won't ever be more pellets than you can express in that 
many digits.

For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

-- Java cases --
Input:
Solution.solution('4')
Output:
    2

Input:
Solution.solution('15')
Output:
    5
'''
def solution(n):
    '''
    It is easy to derive that n must be divided by 2 if n is even. To dicuss
    conveninetly, transform n into the 2-based form. If n is prefixed by m
    zeros, solution(n) should equal to solution(n >> m) + m. For example,
    solution(0b10100) is as the same as solution(0b101) + 2. Basing on this
    rule, We know the number of bits of n must not be reduced when n is odd, so
    our purpose is making n as an even number and doing right shift. Let's 
    consider a function f that returns the pair of minimum numbers of steps to
    reduce a number which is only composed with k bits of 1 to 0 or 1 after 
    doing k times of right shift. For example, f(0b111) returns the numbers of 
    the steps of

    0b111 -> 0b110 => 0b11 -> 0b10 => 0b1 -> 0b0 => 0b0 and
    0b111 -> 0b1000 => 0b100 => 0b10 => 0b1
    (=> means the right shift operation)
    So we get f(0b111) = (6, 4)

    Following the defination of f, we can split n by zero. Take 0b101011 for
    example:

    solution(0b101011) = min(
        solution(0b1011) + f(0b11)[1], 
        solution(0b1010) + f(0b11)[0])

    We can create two small tables to find out the general rule to determine
    which of solution(0b1011) + f(0b11)[1] and solution(0b1010) + f(0b11)[0] is
    the minimum.

    solution(0b11) - solution(0b10) = 2 - 1 = 1
    solution(0b111) - solution(0b110) = 4 - 3 = 1
    solution(0b1111) - solution(0b1110) = 5 - 5 = 0
    solution(0b11111) - solution(0b11110) = 6 - 6 = 0

    k | f((1<<k)-1)[0] | f((1<<k)-1)[1]
    ------------------------------------
    1 |              2 |              2
    2 |              3 |              4
    3 |              4 |              6
    4 |              5 |              8
    k |            k+1 |            2*k

    From above tables, we get if k is 1 f((1<<k)-1)[0] is the better choice
    because it will not change the last bit of the next part of n to 1 in that
    may cause the result of the solution one more number. In other words, if k
    is large or equal to 2, we must choose f((1<<k)-1)[1].

    At last, considering the case that n is only composed with k 1s.
    solution((1<<k)-1) = min(solution(1<<k)+1, solution(1<<k-1)+2)
    It is easy to verify when k >= 3, solution(1<<k)+1 <= solution(1<<k-1)+2.

    With comining all the discussion above, take 0b11001011 for example.
    One of the correct path as the following:
    0b11001011 -> 
    0b11001100 ->
    0b1100110  ->
    0b110011   ->
    0b110100   ->
    0b11010    ->
    0b1101     ->
    0b1100     ->
    0b110      ->
    0b11       ->
    0b10       ->
    0b1        
    '''
    n = int(n)
    ans = 0
    cnt = 0
    while n:
        if n & 1:
            cnt += 1
        else:
            if cnt == 0:
                ans += 1
            elif cnt == 1:
                ans += cnt + 1 + 1
                cnt = 0
            else:
                ans += cnt + 1
                cnt = 1
        n >>= 1
    ans += 2 * cnt - 2 if cnt < 3 else cnt + 1
    return ans
