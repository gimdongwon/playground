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


resorted()