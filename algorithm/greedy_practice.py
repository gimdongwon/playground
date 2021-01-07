# 거스름돈 문제

def remainMoney():
    result = 0
    remain = 1260

    money = [500, 100, 50, 10]
    for i in money:
        if remain != 0:
            result += remain//i
            remain %= i
    print(result)

def bigNum():
    n,m,k = 5,8,3
    param = [2,4,5,4,6]
    result = 0
    count = 1

    param.sort(reverse=True)

    for i in range(m):
        if count <= k:
            result+=param[0]
        else:
            result+=param[1]
            count = 0
        count+=1
    print(result)

def cardGame():
    # card = [[3,1,2],[4,1,4],[2,2,2]]
    card = [[7,3,1,8],[3,3,3,4]]    
    result = []

    for item in card:
        result.append(min(item))
    
    print(max(result))

def gotoOne():
    N,K = 25,5
    count = 0
    while True:
        if N == 1:
            # return count
            break
        if N % K == 0:
            N /= K
        else:
            N -= 1
        count+=1
    print(count)

gotoOne()