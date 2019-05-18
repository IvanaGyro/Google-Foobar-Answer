'''
Running with Bunnies
====================

You and your rescued bunny prisoners need to get out of this collapsing death 
trap of a space station - and fast! Unfortunately, some of the bunnies have been 
weakened by their long imprisonment and can't run very fast. Their friends are 
trying to help them, but this escape would go a lot faster if you also pitched 
in. The defensive bulkhead doors have begun to close, and if you don't make it 
through in time, you'll be trapped! You need to grab as many bunnies as you can 
and get through the bulkheads before they close. 

The time it takes to move from your starting point to all of the bunnies and to 
the bulkhead will be given to you in a square matrix of integers. Each row will 
tell you the time it takes to get to the start, first bunny, second bunny, ..., 
last bunny, and the bulkhead in that order. The order of the rows follows the 
same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, 
so picking them up is instantaneous, and arriving at the bulkhead at the same 
time as it seals still allows for a successful, if dramatic, escape. (Don't 
worry, any bunnies you don't pick up will be able to escape with you since they 
no longer have to carry the ones you did pick up.) You can revisit different 
spots if you wish, and moving to the bulkhead doesn't mean you have to 
immediately leave - you can move to and from the bulkhead to pick up additional 
bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with 
the space station's security checkpoints and add time back to the clock. Adding 
time to the clock will delay the closing of the bulkhead doors, and if the time 
goes back up to 0 or a positive number after the doors have already closed, it 
triggers the bulkhead to reopen. Therefore, it might be possible to walk in a 
circle and keep gaining time: that is, each time a path is traversed, the same 
amount of time is used or added.

Write a function of the form solution(times, time_limit) to calculate the most 
bunnies you can pick up and which bunnies they are, while still escaping through 
the bulkhead before the doors close for good. If there are multiple sets of 
bunnies of the same size, return the set of bunnies with the lowest prisoner IDs 
(as indexes) in sorted order. The bunnies are represented as a sorted list by 
prisoner ID, with the first bunny being 0. There are at most 5 bunnies, and 
time_limit is a non-negative integer that is at most 999.

For instance, in the case of
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
and a time limit of 1, the five inner array rows designate the starting point, 
bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could 
take the path:

Start End Delta Time Status
    -   0     -    1 Bulkhead initially open
    0   4    -1    2
    4   2     2    0
    2   4    -1    1
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best 
combination for this space station hallway, so the answer is [1, 2].

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
Solution.solution({
    {0, 1, 1, 1, 1},
    {1, 0, 1, 1, 1},
    {1, 1, 0, 1, 1},
    {1, 1, 1, 0, 1},
    {1, 1, 1, 1, 0}}, 3)
Output:
    [0, 1]

Input:
Solution.solution({
    {0, 2, 2, 2, -1},
    {9, 0, 2, 2, -1},
    {9, 3, 0, 2, -1},
    {9, 3, 2, 0, -1},
    {9, 3, 2, 2, 0}}, 1)
Output:
    [1, 2]

-- Python cases --
Input:
solution.solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0]], 1)
Output:
    [1, 2]

Input:
solution.solution([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]], 3)
Output:
    [0, 1]

Use verify [file] to test your solution and see how it does. When you are 
finished editing your code, use submit [file] to submit your answer. If your 
solution passes the test cases, it will be removed from your home folder.
'''
inf = float('inf')
from collections import defaultdict
def solution(times, times_limit):
    '''
    Answers(2019.05.12): 
    Case 1: [1, 2]
    Case 2: [0, 1]
    Case 3: [0, 1, 2, 3, 4]
    Case 4: []
    Case 5: [0, 2, 3, 4]
    Case 6: [0, 1, 2]
    Case 7: [0, 1, 2, 3, 4]
    Case 8: [1, 2, 3]
    Case 9: [0, 2, 4]
    Case 10: [0, 1, 2, 3, 4]

    Case 3:
    solution([
        [ 0,  1, -2,  3,  2, -1,  0],
        [-1,  0, -3,  2,  1, -2, -1],
        [ 2,  3,  0,  5,  4,  1,  2],
        [-3, -2, -5,  0, -1, -4, -3],
        [-2, -1, -4,  1,  0, -3, -2],
        [ 1,  2, -1,  4,  3,  0,  1],
        [ 0,  1, -2,  3,  2, -1,  0]], 0)

    Case 7:
    solution([
        [0, 99, 99, 99, 99, 99, -1],
        [99, 0, 99, 99, 99, 99, 99],
        [99, 99, 0, 99, 99, 99, 99],
        [99, 99, 99, 0, 99, 99, 99],
        [99, 99, 99, 99, 0, 99, 99],
        [99, 99, 99, 99, 0, 0, 99],
        [0, 99, 99, 99, 99, 99, 0]], 1)

    Case 8:
    solution([
        [0 , 15, 19, 10, -1, 12,  4], 
        [7 ,  0, 19,  4, 19, 17,  7], 
        [15,  8,  0, 14,  8,  4,  3], 
        [10, 14,  6,  0,  0,  5,  9], 
        [18,  8,  4,  0,  0, 12, 16], 
        [0 , 13,  1, -1, 12,  0,  4], 
        [8 ,  5,  2, 11, 12, 16,  0]], 7)
    
    Case 10:
    solution([
        [ 0,  3, 82, 91, 15, 24, 77],
        [ 8,  0,  7, 32,  6, 33, 14],
        [66, 98,  0, 62, 59,  5, 39],
        [64, 97,  5,  0, 45, 84, 21],
        [ 3, 33, 81, 24,  0, 53,  5],
        [73, 93, 29,  9, 78,  0, 44],
        [70, 76, 15,  0, 43, 58,  0]], 999)
    '''
    if not times or len(times) != len(times[0]):
        return []

    n = len(times)

    arrive_time = [inf]*n
    circles = [defaultdict(lambda: inf) for _ in range(n)]
    single_paths = defaultdict(lambda: inf)

    def find_valid_path(path, state, time):
        if state in path:
            diff = time - arrive_time[state]
            if diff >= 0:
                circle = path[path.index(state):]
                circle = tuple(sorted(p for p in circle if 0 < p < n-1))
                if len(circle) == n - 2 and diff == 0:
                    return True
                if len(circle) > 0 and circle != (state,):
                    circles[state][circle] = min(
                        circles[state][circle], 
                        diff
                    )
            return diff < 0
        else:
            total_time = time + times[state][-1]
            if total_time <= times_limit:
                total_time = time + times[state][-1]
                full_path = path[1:] + (state,)
                single_paths[full_path] = min(
                    single_paths[full_path],
                    total_time,
                )
            arrive_time[state] = min(time, arrive_time[state])
            return any(
                find_valid_path(path + (state,), i, time+times[state][i]) 
                for i in range(n)
            )

    if find_valid_path((), 0, 0):
        return list(range(n-2))

    for i in range(n):
        tmp = defaultdict(list)
        for c, t in circles[i].items():
            tmp[t].append(set(c))
        zero = set()
        for c in tmp[0]:
            zero |= c
        tmp[0] = [zero]
        circles[i] = tmp

    max_bunnies = [0]
    bunnies = defaultdict(lambda: times_limit)

    def flood_zero(c):
        while True:
            for i in c:
                if circles[i][0][0] - c:
                    c = flood_zero(c | circles[i][0][0])
                    break
            else:
                break
        for i in c:
            circles[i][0][0] |= c
        return c

    for i in range(n):
        flood_zero(circles[i][0][0])

    def combine(p, t):
        max_bunnies[0] = max(max_bunnies[0], len(p))
        
        p_ = tuple(sorted(p))
        if t < bunnies[p_]:
            bunnies[p_] = t
            for i in p | set((0, n -1)):
                for diff in range(1, times_limit - t + 1):
                    for c in circles[i][diff]:
                        combine(p | c, t + diff)

    for p, time in single_paths.items():
        p = set(p)
        for i in p.copy():
            p |= circles[i][0][0]
        p -= set((0, n-1))
        combine(p, time)

    res = sorted(list(b) for b in bunnies if len(b) == max_bunnies[0])
    return [r - 1 for r in res[0]] if res else []


def test():
    res = solution([
        [0, 2, 9, 9, 1],
        [9, 0, 9, 2, 1],
        [9, 9, 0, 9, -1],
        [9, 9, 9, 0, -4],
        [9, 9, 9, 9, 0]], -20)
    assert res == []

    res = solution([
        [0, 2, 2, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0]], 1)
    assert res == [1, 2], res

    res = solution([
        [0 , 15, 19, 10, -1, 12,  4], 
        [7 ,  0, 19,  4, 19, 17,  7], 
        [15,  8,  0, 14,  8,  4,  3], 
        [10, 14,  6,  0,  0,  5,  9], 
        [18,  8,  4,  0,  0, 12, 16], 
        [0 , 13,  1, -1, 12,  0,  4], 
        [8 ,  5,  2, 11, 12, 16,  0]], 7)
    assert res == [1, 2, 3]

    res = solution([
        [0 ,  0, 19, 19, 19, 19, 19], 
        [7 ,  0,  0, 19, 19, 17, 19], 
        [19, 19,  0,  0,  0,  5, 19], 
        [10,  0, 19,  0, 19, 19, 19], 
        [19,  0, 19, 19,  0, 19, 19], 
        [19, 19, 19, 19, 19,  0,  2], 
        [8 ,  6,  6, 11, 12, 16,  0]], 7)
    assert res == [0, 1, 2, 3, 4]

    res = solution([
        [0, 19, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 19, 0, 1, 1],
        [1, 19, 1, 0, 1],
        [1, 19, 1, 1, 0]], 3)
    assert res == [1, 2]

    res = solution([
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0]], 3)
    assert res == [0, 1]

    res =  solution([
        [ 0,  3, 82, 91, 15, 24, 77],
        [ 8,  0,  7, 32,  6, 33, 14],
        [66, 98,  0, 62, 59,  5, 39],
        [64, 97,  5,  0, 45, 84, 21],
        [ 3, 33, 81, 24,  0, 53,  5],
        [73, 93, 29,  9, 78,  0, 44],
        [70, 76, 15,  0, 43, 58,  0]], 999)
    assert res == [0, 1, 2, 3, 4]

    res = solution([
        [ 0,  1, -2,  3,  2, -1,  0],
        [-1,  0, -3,  2,  1, -2, -1],
        [ 2,  3,  0,  5,  4,  1,  2],
        [-3, -2, -5,  0, -1, -4, -3],
        [-2, -1, -4,  1,  0, -3, -2],
        [ 1,  2, -1,  4,  3,  0,  1],
        [ 0,  1, -2,  3,  2, -1,  0]], 0)
    assert res == [0, 1, 2, 3, 4]

    res = solution([
        [0 ,  0, 19, 19, 19, 19, 19], 
        [7 ,  0,  0, 19,  0, 17, 19], 
        [19, 19,  0,  0, 19,  5, 19], 
        [10,  0, 19,  0, 19, 19, 19], 
        [19, 19, 19, 19,  0,  0, 19], 
        [19,  0, 19, 19, 19, 19,  2], 
        [8 ,  6,  6, 11, 12, 16,  0]], 7)
    assert res == [0, 1, 2, 3, 4]

    res = solution([
        [0, 99, 99, 99, 99, 99, -1],
        [99, 0, 99, 99, 99, 99, 99],
        [99, 99, 0, 99, 99, 99, 99],
        [99, 99, 99, 0, 99, 99, 99],
        [99, 99, 99, 99, 0, 99, 99],
        [99, 99, 99, 99, 0, 0, 99],
        [0, 99, 99, 99, 99, 99, 0]], 1)
    assert res == [0, 1, 2, 3, 4], res

test()
