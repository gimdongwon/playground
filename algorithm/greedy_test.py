# 1. 모험가 빌드

def adventurer():
    x = [2,3,1,2,2]

    current = 0
    result = 0
    x.sort(reverse=True)

    for i in range(0, len(x)):
        if i < current:
            continue
        group = x[current:current+x[i]]
        current += len(group)
        result += 1
    print(result)

# adventurer()

# 곱하기 혹은 더하기

def addORmultiply():
    result = 0
    param = "02984"
    param2 = "567"

    target = list(param)
    for i in range(len(target)):
        if result==0 or int(target[i]) < 2:
            result+=int(target[i])
        else:
            result*=int(target[i])
    
    print(result)

# addORmultiply()

# 문자열 뒤집기

def strReverse():
    param = "0100110"
    result = 0

    target = list(param)
    targetNum = "0" if target.count("0") < target.count("1") else "1"
    
    for i in range(0,len(target)-1):
        if targetNum == target[i] and targetNum != target[i+1]:
            result+=1
    print(result)

# strReverse()

def donotMakeMoney():
    param = [3,2,1,1,9]
    param.sort(reverse=True)
    
    for i in range(1, sum(param)):
        if param.count(i)>0:
            continue
        result = i
        for j in param:
            if result >= j:
                result-=j
        if result!=0:
            print(i)


# donotMakeMoney()

def selectBall():
    from itertools import combinations
    param = [1,3,2,3,2] # 8
    param2 = [1,5,4,3,2,4,5,2] # 25

    diff = len(param2) - len(set(param2))

    print(len(list(combinations(param2, 2))) - diff)


selectBall()