def solution(numbers):
    resultList = [];
    for i in range(len(numbers)-2):
        if numbers[i] < numbers[i+1] > numbers[i+2] or numbers[i] > numbers[i+1] < numbers[i+2]:
            resultList.append(1)
        else:
            resultList.append(0)
    return resultList

print(solution([1,2,1,3,4]))
print(solution([1,2,3,4]))
print(solution([1000000000, 1000000000, 1000000000]))

