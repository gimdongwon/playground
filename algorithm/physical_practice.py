# 상하좌우


def direction():
    N = 5
    movement = ["R", "R", "R", "U", "D", "D"]

    x, y = 1, 1

    for item in movement:
        if item == "R":
            if y < N:
                y += 1
        elif item == "U":
            if x > 1:
                x -= 1
        elif item == "D":
            if x < N:
                x += 1
        else:
            if y > 1:
                y -= 1
    print(x, y)


# direction()

# 시각


def clock(N):
    result = 0

    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                # if (str(i) + str(j) + str(k)).count("3"): # 내 풀이
                if "3" in str(i) + str(j) + str(k):  # 책 풒ㄹ이
                    result += 1
    print(result)


# clock(5)

# 왕실의 나이트


def knight(N):
    steps = [(1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (1, -2), (-2, 1), (2, -1)]
    current = list(N)
    result = 0

    x = ord(current[0]) - ord("a") + 1
    y = int(current[1])
    for i in steps:
        if i[0] + x > 0 and i[0] + x < 9:
            if i[1] + y > 0 and i[1] + y < 9:
                result += 1
    print(result)


# knight("d4")

# 게임 개발


def game():
    result = 1
    miniMap = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
    current = [1, 1, 0]

    count = 0

    while count < 4:
        if current[2] == 0:  # 북
            if current[1] == 0 or miniMap[current[0]][current[1] - 1] == 1:
                current[2] = 3
                count += 1
            else:
                miniMap[current[0]][current[1]] = 1
                current[1] -= 1
                count = 0
                result += 1
        elif current[2] == 1:  # 동
            if current[1] == 4 or miniMap[current[0]][current[1] + 1] == 1:
                current[2] = 0
                count += 1
            else:
                miniMap[current[0]][current[1]] = 1
                current[1] += 1
                count = 0
                result += 1
        elif current[2] == 2:  # 남
            if current[0] == 4 or miniMap[current[0] + 1][current[1]] == 1:
                current[2] = 1
                count += 1
            else:
                miniMap[current[0]][current[1]] = 1
                current[0] += 1
                count = 0
                result += 1
        else:  # 서
            if current[0] == 0 or miniMap[current[0] - 1][current[1]] == 1:
                current[2] = 2
                count += 1
            else:
                miniMap[current[0]][current[1]] = 1
                current[0] -= 1
                count = 0
                result += 1
    print(result)


# 게임 개발 책 솔루션


def gameSolution():
    # N, M을 공백을 기준으로 구분하여 입력받기
    n, m = map(int, input().split())

    # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    d = [[0] * m for _ in range(n)]
    # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
    x, y, direction = map(int, input().split())
    d[x][y] = 1  # 현재 좌표 방문 처리

    # 전체 맵 정보를 입력받기
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    # 북, 동, 남, 서 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        direction -= 1
        if direction == -1:
            direction = 3

        nx = x + dx[direction]
        ny = y + dy[direction]
        # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1
        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동하기
            if array[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다로 막혀있는 경우
            else:
                break
            turn_time = 0

    # 정답 출력
    print(count)


gameSolution()