# 1. 모험가 빌드

"""
나는 그룹의 최댓수를 늘리는 것이 아무도 빠짐 없이 넣는것이라 생각해서 내림 차순으로 정렬을 하였는데 
그룹의 최댓수는 남는 사람이 있다 하더라도 공포도가 높은 사람을 그룹핑하는 것이 최대 그룹수를 형성하는 것이었다.
이를 고쳐보면
"""


def adventurer():
    x = [2, 3, 1, 2, 2]

    current = 0
    result = 0
    x.sort(reverse=False)

    for i in range(0, len(x)):
        if i < current:
            continue
        group = x[current : current + x[i]]
        current += len(group)
        result += 1
    print("adventurer : ", result)


def fixAdventurer():
    x = [2, 3, 1, 2, 2]

    current = 0
    result = 0
    x.sort()

    for i in range(len(x)):
        current += 1
        if x[i] >= current:
            result += 1
            current = 0
    print(result)


# fixAdventurer()

# -------------------------------

# 곱하기 혹은 더하기


def addORmultiply():
    result = 0
    param = "02984"
    param2 = "567"

    target = list(param)
    for i in range(len(target)):
        currentNum = int(target[i])
        if result == 0 or currentNum < 2:
            result += currentNum
        else:
            result *= currentNum

    print(result)


# addORmultiply()

# -----------------

# 문자열 뒤집기
# 더 적은 횟수로 뒤집는 경우로 계산


def strReverse():
    param = "0100110"
    result = 0

    target = list(param)
    targetNum = "0" if target.count("0") < target.count("1") else "1"

    for i in range(0, len(target) - 1):
        if targetNum == target[i] and targetNum != target[i + 1]:
            result += 1
    print(result)


# strReverse()

"""
타겟을 정하여 해당 숫자를 만들 수 있으면 그 아랫 숫자들은 다 만들 수 있다.
"""

def donotMakeMoney():
    param = [3, 2, 1, 1, 9]
    # param = [1, 2, 3, 8]
    param.sort(reverse=True)

    for i in range(1, sum(param)):
        if param.count(i) > 0:
            continue
        result = i
        for j in param:
            if result >= j:
                result -= j
        if result != 0:
            print(i)

def bookDonotMakeMoney():
    param = [3, 2, 1, 1, 9]
    param.sort()
    target = 1

    for i in param:
        if target<i:
            break
        target += i
    print(target)

bookDonotMakeMoney()

# --------------------

# 볼링공 고르기

# 내 방법이 더 효율적인듯

def selectBall():
    from itertools import combinations

    param = [1, 3, 2, 3, 2]  # 8
    param2 = [1, 5, 4, 3, 2, 4, 5, 2]  # 25

    diff = len(param2) - len(set(param2))

    print(len(list(combinations(param2, 2))) - diff)


# selectBall()

# 무지의 먹방 라이브

# 1차시도
# def solution(food_times, k):
#     for i in range(k):
#         current = i % len(food_times)
#         if food_times[current] != 0:
#             food_times[current] -= 1
#         else:
#             while True:
#                 current+=1
#                 if current > len(food_times):
#                     current %= len(food_times)
#                 if food_times[current] !=0:
#                     break
#             food_times[current]-=1
#         if [0]*len(food_times) == food_times:
#             return -1
#     return (current+1) % len(food_times) + 1

# 2차시도
# def solution(food_times, k):
#     if sum(food_times) <=k:
#         return -1
#     curMin = min(food_times)
#     if curMin != 0:
#         k -=  curMin*len(food_times)
#         for i in range(len(food_times)):
#             food_times[i] -= curMin

#     print(food_times)

# 정답
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
        print(f"{sum_value}, {q}, previous : {previous}, leng: {length}, now: {now}")

    result = sorted(q, key=lambda x: x[1])
    print(result)
    return result[(k - sum_value) % length][1]
