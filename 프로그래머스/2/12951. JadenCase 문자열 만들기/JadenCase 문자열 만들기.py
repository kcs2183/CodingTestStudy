def solution(s):
    word = []
    answer = ''

    for w in s.split(' '):
        if len(w) > 0 and w[0].isalpha():
            word.append(w[0].upper() + w[1:].lower())
        else:
            word.append(w.lower())

    answer = ' '.join(word)
    return answer