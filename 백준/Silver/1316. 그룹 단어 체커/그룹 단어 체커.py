n = int(input())
count = n

for _ in range(n):
    word = input()
    alphabets = set(word)

    for alphabet in alphabets:
        current_alphabet_count = word.count(alphabet)

        if len(set(word[word.index(alphabet):word.index(alphabet) + current_alphabet_count])) > 1:
            count -= 1
            break

print(count)