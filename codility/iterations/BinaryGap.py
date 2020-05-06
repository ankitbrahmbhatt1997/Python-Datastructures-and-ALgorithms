

def decToBinary(n):
    return bin(n).replace("0b","")

def findSequence(n):
    sequenceStart = False
    sequenceClosed = False
    max_sequence = 0
    currentCount = 0
    binaryNumber = decToBinary(n)
    for i in binaryNumber:
        # print(i)
        if int(i)==1 and not sequenceStart:
            sequenceStart = True
        if int(i)==0 and sequenceStart and not sequenceClosed:
            currentCount+=1
        if int(i)==1 and sequenceStart and not sequenceClosed:
            max_sequence = max(max_sequence,currentCount)
            currentCount = 0
    return max_sequence
            

print(findSequence(1041))