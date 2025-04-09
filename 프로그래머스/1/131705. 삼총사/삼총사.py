def solution(number):
    count = 0

    for i, value1 in enumerate(number):
        for j, value2 in enumerate(number):
            for k, value3 in enumerate(number):
                if value1 + value2 + value3 == 0 and i < j and j < k:
                    count += 1

    answer = count
    return answer



number = [-3, -2, -1, 0, 1, 2, 3]
print(solution(number))