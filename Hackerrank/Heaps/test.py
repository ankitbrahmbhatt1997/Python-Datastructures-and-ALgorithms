from sys import stdin

tasks = []
for _ in range(3):
    A,C = map(int,stdin.readline().strip().split(" "))
    tasks.append((A,C))

tasks.sort(reverse=True)
print(tasks.pop()[::-1])