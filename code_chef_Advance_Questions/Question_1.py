############################QUESTION###########################################

# During the Indian Programming Camp (IPC), there are N trainers. The camp runs for D days. Each day, there can be at most one lecture. The i-th trainer arrives on day Di and then stays till the end of the camp. He also wants to teach exactly Ti lectures. For each lecture that a trainer was not able to teach, he will feel sad and his sadness level will be increased by Si.

# You are the main organizer of the contest. You want to find minimum total sadness of the trainers.


#########################################INPUT###########################

# The first line of the input contains an integer T, denoting the number of testcases.

# For each test case, the first line contains two space separated integers, N, D.

# The i-th of the next N lines will contain three space separated integers: Di, Ti, Si respectively.

# OUTPUT

# For each test case, output a single integer corresponding to the minimum total sadness of the trainers achievable.


# Example
# Input
# 3
# 2 3
# 1 2 300
# 2 2 100
# 2 3
# 1 1 100
# 2 2 300
# 2 3
# 3 2 150
# 1 1 200

# Output
# 100
# 0
# 150


######################################SOLUTION################################################
from sys import stdin
from heapq import heappush,heapify,heappop


def calculate(N, D, info):
    sortedInfo = sorted



t = int(stdin.readline())
for i in range(t):
    N, D = map(int, stdin.readline().strip("").split(" "))
    info = []
    for j in range(N):
        d, t, s = map(int, stdin.readline().strip().split(" "))
        info.append((d, t, s))
    minSadness = calculate(N, D, info)
