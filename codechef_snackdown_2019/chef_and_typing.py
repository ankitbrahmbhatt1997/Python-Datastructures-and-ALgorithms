from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    words = []
    for j in range(n):
        words.append(stdin.readline().strip())
    record = {}
    Total = 0
    for single_word in words:
        if single_word in record:
            Total = Total+record[single_word]/2
            continue
        word_total = 0
        for k in range(0, len(single_word)):
            if k == 0:
                word_total += 0.2
            else:
                if single_word[k-1] == 'd' or single_word[k-1] == 'f':
                    if single_word[k] == 'd' or single_word[k] == 'f':
                        word_total += 0.4
                    else:
                        word_total += 0.2
                elif single_word[k-1] == 'j' or single_word[k-1] == 'k':
                    if single_word[k] == 'j' or single_word[k] == 'k':
                        word_total += 0.4
                    else:
                        word_total += 0.2

        Total += word_total
        record[single_word] = word_total

    print(int(Total*10))
