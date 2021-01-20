# 럭키 스트레이트


def luckyStraight():
    s = input()
    mid = len(s) // 2

    left = list(s[:mid])
    right = list(s[mid:])

    leftSum, rightSum = 0, 0

    for i in range(len(left)):
        leftSum += int(left[i])
        rightSum += int(right[i])

    if leftSum == rightSum:
        print("LUCKY")
    else:
        print("READY")


# luckyStraight()

# ---

# 문자열 재정렬


def resorted():
    s = input()
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    result = 0
    result2 = ""
    target = list(s)
    target.sort()

    for item in target:
        if item in nums:
            result += int(item)
        else:
            result2 += item
    print(result2 + str(result))


# resorted()

# ----

# 문자열 압축


def solution(s):
    if len(s) == 1:
        return 1
    target = []
    result = []

    for i in range(1, (len(s) // 2) + 1):
        sList = [s[j : j + i] for j in range(0, len(s), i)]
        target.append(sList)

    for item in target:
        count = 1
        temp = ""
        for i in range(0, len(item)):
            if i != len(item) - 1 and item[i] == item[i + 1]:
                count += 1
            else:
                if count > 1:
                    temp += str(count) + item[i]
                else:
                    temp += item[i]
                count = 1
        result.append(temp)
    result.sort(key=len)
    return len(result[0])


# ------

# 자물쇠와 열쇠

import copy

# M*M 사이즈 key를 회전해서 만든 4가지 key 배열을 반환
def rotate(key):
    ret = []
    m = len(key)
    for i in range(4):
        temp = [[0 for i in range(m)] for j in range(m)]  # 0으로 초기화
        for i in range(m):
            for j in range(m):
                temp[m - j - 1][i] = key[i][j]
        key = temp
        ret.append(temp)

    return ret


# 열리는지 확인하는 함수
# (zero padding map, key list, start index1, start index2, key size, lock size)
def isUnLock(lock_map, keys, i, j, key_size, lock_size):
    # zero padding map에서 lock부분의 시작과 끝 인덱스
    lock_start = key_size - 1
    lock_end = lock_size + key_size - 2

    # 4가지 key에 대해서 시작 인덱스에서 key와 lock 값을 더한 map만듬
    for key in keys:
        temp = copy.deepcopy(lock_map)
        for x in range(i, i + key_size):
            for y in range(j, j + key_size):
                if (
                    x >= lock_start
                    and x <= lock_end
                    and y >= lock_start
                    and y <= lock_end
                ):
                    temp[x][y] += key[x - i][y - j]

        # lock 영역이 모두 1인지 체크
        flag = True
        for x in range(lock_start, lock_end + 1):
            for y in range(lock_start, lock_end + 1):
                if temp[x][y] != 1:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            return True

    return False


def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    # zero padding
    lock_map = [[0 for i in range(n + m * 2 - 2)] for j in range(n + m * 2 - 2)]
    for i in range(m - 1, n + m - 1):
        for j in range(m - 1, n + m - 1):
            lock_map[i][j] = lock[i - m + 1][j - m + 1]

    # 모든 영역돌면서 체크
    keyList = rotate(key)
    for i in range(n + m - 1):
        for j in range(n + m - 1):
            if isUnLock(lock_map, keyList, i, j, m, n):
                return True

    return answer


# 자물쇠와 열쇠 book solution


def rotate(key):

    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠를 기존의 크기의 3배로 설정
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate(key)  # rotate key
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


# 기둥과 보

# 초기 답 - 오답


def solution(n, build_frame):
    answer = []
    map = [[0] * n for _ in range(len(build_frame))]

    for item in build_frame:
        site = item[0:2]
        types = item[2]
        status = item[3]

        if status == 1:  # 설치
            if types == 0:  # 기둥 설치
                if item[1] < 1:
                    answer.append(item[0:3])
                elif [item[0] - 1, item[1], 1] in answer or [
                    item[0],
                    item[1] - 1,
                    0,
                ] in answer:
                    answer.append(item[0:3])
            else:  # 보 설치
                if item[1] != 0:  # 보가 바닥에
                    answer.append(item[0:3])
        # 삭제
        else:
            # 기둥삭제
            if types == 0:
                if (
                    item[1] == 0
                    or [item[0], item[1], 1] in answer
                    and [item[0] - 1, item[1] + 1, 1] in answer
                ):
                    answer.remove(item[0:3])
            # 보삭제
            else:
                if [item[0] + 1, item[1] - 1, 0] in answer:
                    answer.remove(item[0:3])

    answer.sort()
    return answer

def chicken():
    from itertools import combinations
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    home = []
    chickenHome = []
    distance = 0
    distanceZip = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i,j])
            elif arr[i][j] == 2:
                chickenHome.append([i,j])
    result = chickenHome
    if M != 1:
        result = list(combinations(chickenHome, M))
        for resultItem in result:
            distance = 0
            for homeItem in home:
                temp = []
                for resultItem2 in resultItem:
                    temp.append(abs(resultItem2[0]-homeItem[0]) + abs(resultItem2[1]-homeItem[1]))
                distance += min(temp)
            distanceZip.append(distance)
    else:
        for resultItem in result:
            distance = 0
            for homeItem in home:
                distance += abs(resultItem[0] - homeItem[0]) + abs(resultItem[1] - homeItem[1])
            distanceZip.append(distance)
    
    print(min(distanceZip))
    

# chicken()

def wallInspection(n, weak, dist):
    from itertools import permutations
    length = len(weak)
    # 길이를 두배로 늘려서 일자 형태로 변경
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
    # 0부터 length-1 까지의 위치를 각각의 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            position = weak[start]+friends[count-1] # 해당 친구가 점검할 수 있는 마지막 위치
            for index in range(start, start+length): # 시작점부터 모든 취약지점을 확인
                if position<weak[index]: # 점검할 수 있는 위치를 벗어나는 경우
                    count+=1 # 새로운 친구 투입
                    if count>len(dist): # 더 ㅌ투입이 불가능 하다면 종료
                        break
                    position = weak[index]+friends[count-1]
            answer = min(answer, count) # 최솟값 계산
    # 다 투입해도 취약 지점을 전부 보수할 수 없는 경우.
    if answer > len(dist):
        return -1
    return answer