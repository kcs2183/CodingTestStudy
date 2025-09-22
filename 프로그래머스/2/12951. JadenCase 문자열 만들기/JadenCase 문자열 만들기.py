def solution(s):
    word = []
    answer = ''

    for w in s.split(' '):
        if w.isalpha():
            word.append(w[0].upper() + w[1:].lower())
        else:
            word.append(w.lower())

    answer = ' '.join(word)
    return answer