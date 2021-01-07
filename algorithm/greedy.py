# 함수 작성

# 1. 큰수의 법칩
def bigNum():
    N,M,K = map(int,input().split())
    data = list(map(int, input().split()))

    maxNum = max(data)
    data.remove(maxNum)
    secondMaxNum = max(data)
    
    result = 0
    duplication = 0
    for i in range(M):
        duplication +=1
        if duplication <= K:
            result += maxNum
        else:
            result+=secondMaxNum
            duplication = 0
    print(result)

# 결과 출력
bigNum()