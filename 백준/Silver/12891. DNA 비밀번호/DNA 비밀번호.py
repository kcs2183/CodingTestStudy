from sys import stdin

s, p = map(int, stdin.readline().split())
dna_str = stdin.readline().rstrip()
min_a, min_c, min_g, min_t = map(int, stdin.readline().split())

answer = 0

a_cnt = dna_str[0:p].count('A')
c_cnt = dna_str[0:p].count('C')
g_cnt = dna_str[0:p].count('G')
t_cnt = dna_str[0:p].count('T')

if a_cnt >= min_a and c_cnt >= min_c and g_cnt >= min_g and t_cnt >= min_t:
        answer += 1

for i in range(s-p):
    if dna_str[i] == 'A':
        a_cnt -= 1
    elif dna_str[i] == 'C':
        c_cnt -= 1
    elif dna_str[i] == 'G':
        g_cnt -= 1
    elif dna_str[i] == 'T':
        t_cnt -= 1

    if dna_str[i+p] == 'A':
        a_cnt += 1
    elif dna_str[i+p] == 'C':
        c_cnt += 1
    elif dna_str[i+p] == 'G':
        g_cnt += 1
    elif dna_str[i+p] == 'T':
        t_cnt += 1
    
    if a_cnt >= min_a and c_cnt >= min_c and g_cnt >= min_g and t_cnt >= min_t:
        answer += 1

print(answer)