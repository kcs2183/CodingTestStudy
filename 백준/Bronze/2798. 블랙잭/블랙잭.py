def blackjack(n, m, card):
    answer = 0

    for i in range(n-2):
        sum = 0
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                sum = card[i] + card[j] + card[k]
                if sum <= m and answer < sum:
                    answer = sum
    
    return answer

n, m = map(int, input().split())
cards = list(map(int, input().split()))
print(blackjack(n, m, cards))