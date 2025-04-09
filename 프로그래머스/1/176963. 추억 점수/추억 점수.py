def solution(name, yearning, photo):
    dict = {}
    result = []

    for i in range(len(name)):
        dict[name[i]] = yearning[i]

    for i in photo:
        sum = 0
        for j in i:
            if j in dict.keys():
                sum += dict[j]
        result.append(sum)

    answer = result
    return answer