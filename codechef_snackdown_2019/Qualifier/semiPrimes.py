
from sys import stdin
import math


def checkSemiprime(num):
    cnt = 0
    dict = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            dict.append(i)
            cnt += 1

        if cnt >= 2:
            break

    if(num > 1):
        dict.append(num)
        cnt += 1

    if cnt == 2:
        if dict[0] != dict[1]:
            return True
        else:
            return False
    else:
        return False


# def semiprime(n):

#     if checkSemiprime(n) == True:
#         return True
#     else:
#         return False

t = int(stdin.readline())
for z in range(t):
    sp_dic = {}
    result = "NO"
    fnum = int(stdin.readline())
    for i in range(6, fnum-5):

        if i not in sp_dic:

            if checkSemiprime(i) == True:
                sp_dic[i] = "Y"

                if checkSemiprime((fnum - i)) == True:
                    result = "YES"
                    break
                else:
                    sp_dic[(fnum - i)] = "N"
    print(result)
