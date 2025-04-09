from collections import deque

deque_ = deque([i+1 for i in range(int(input()))])

while len(deque_) > 1:    
    deque_.popleft()
    deque_.append(deque_.popleft())

print(deque_[0])