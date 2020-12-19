def binarySearch(data, target):
    start = 0
    end = len(data)-1

    while start<=end:
        mid = start + end // 2
        # print(mid)
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid - 1

def selfBinarySearch(data, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return selfBinarySearch(data, target, start, end)

print(binarySearch([1,2,3,4,5,6,7,8], 8))
print(selfBinarySearch([1,2,3,4,5,6,7,8], 8, 0, 8))