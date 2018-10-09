from sys import stdin
jacketCost, sockCost, money = map(int, stdin.readline().strip().split(" "))

if ((money-jacketCost)//sockCost) % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")
