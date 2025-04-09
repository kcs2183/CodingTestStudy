t, x = map(int, input().split()) # t 안 쓰임

for _ in range(int(input())):
    input() # v1에서 k에 값 저장을 저장하지 않는 걸로 수정
    
    if x not in map(int, input().split()): # 배열에 저장하지 않고 바로 조건으로 사용
        print('NO')
        exit() # condition 변수를 제거하여 프로그램 종료로 수정

print('YES')