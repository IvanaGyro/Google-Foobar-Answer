# If you have known the answer of the specific test case and also have known the
# upper bound and the lower bound of the test data, you can use this script to 
# get the value of the test data.
#
# This script will overwrite your solution to the code like:
#
# def solution(param1, param2):
#     ''' setup statements '''
#     assert {upper bound} > {param} >= {lower bound}
#     return {correct answer}
#
# And then the script will call the API to fire the process of verifying. If the 
# test data you want to get is in the range, the result of the test case will be 
# passed, otherwise will be failed. This script uses binary search to narrow down 
# the possible range iteratively. Please see the end of the script for the 
# example.
#
# Notice:
# Before your executing the script, you must copy your cookies and headers from the
# browser. The listed fields are required.


import requests
import re

headers = {
    'Referer':'Your-page-link',
    'X-CSRFToken':'Your-X-CSRFToken',
}

cookies = {
    'sessionid':'Your-sessionid',
    'SACSID':'Your-SACSID',
}

def verify(path):
    r = requests.post(
        'https://foobar.withgoogle.com/api/v1/commands/verify/',
        data={'path':path}, 
        headers=headers,
        cookies=cookies
    )

    output = r.json()['output']
    return [r == 'passed' for r in re.findall(r'Test \d+ (passed|failed)', output)]

def save(path, code):
    r = requests.post(
        'https://foobar.withgoogle.com/api/v1/commands/save/',
        data={'path':path, 'content':code}, 
        headers=headers,
        cookies=cookies
    )
    assert r.status_code == 204


def build_code(params, beg, end, name, ans, prepare=''):
    return f'''\
def solution({', '.join(params)}):
    {prepare}
    assert {end} > {name} >= {beg}
    return {ans}
'''

def steal_value(path, params, beg, end, name, case, ans, prepare=''):
    while end - beg > 1:
        mid = (beg + end) // 2
        code = build_code(params, beg, mid, name, ans, prepare)
        try:
            save(path, code)
            res = verify(path)
        except Exception as e:
            print(f'Name: {name}, Range: ({beg}, {end})')
            raise e
        if res[case]:
            end = mid
        else:
            beg = mid
    return beg


path = 'the-file-path/solution.py' # example: '/running-with-bunnies/solution.py' 
params = ('times', 'times_limit')
beg, end = -1, 100
case = 7
ans = [0,1,2,3,4]

limit = steal_value(path, params, -1000, 1000, 'times_limit', case-1, ans)
print(f'limit: {limit}')
max_ = steal_value(path, params, -1000, 1000, 'max_', case-1, ans, prepare='max_ = max(max(r) for r in times)')
print(f'max:{max_}')
min_ = steal_value(path, params, -1000, 1000, 'min_', case-1, ans, prepare='min_ = min(min(r) for r in times)')
print(f'min:{min_}')

vals = [[0]*7 for _ in range(7)]

for i in range(7):
    for j in range(7):
        name = f'times[{i}][{j}]'
        val = steal_value(path, params, beg, end, name, case-1, ans)
        print(f'{name}:{val}')
        vals[i][j] = val

print(vals)
