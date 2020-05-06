def solution(S, P, Q):

    nulcleaData = {
        "A":1,
        "C":2,
        "G":3,
        "T":4
    }

    sumA,sumC,sumG,sumT = [0],[0],[0],[0]

    for i in S:
        if i == "A":
            sumA.append(nulcleaData["A"])
            sumC.append(0)
            sumG.append(0)
            sumT.append(0)
        elif i == "C":
            sumC.append(nulcleaData["C"])
            sumA.append(0)
            sumG.append(0)
            sumT.append(0)
        elif i == "G":
            sumG.append(nulcleaData["G"])
            sumC.append(0)
            sumA.append(0)
            sumT.append(0)
        elif i == "T":
            sumT.append(nulcleaData["T"])
            sumC.append(0)
            sumG.append(0)
            sumA.append(0)

    for i in range(1,len(sumA)):
        sumA[i]+=sumA[i-1]
        sumC[i]+=sumC[i-1]
        sumG[i]+=sumG[i-1]
        sumT[i]+=sumT[i-1]
    minValue = 5
    answers=[]
    # print(sumA,sumC,sumG,sumT)
    for p,q in zip(P,Q):
        # print(p,q)
        if sumA[q+1] - sumA[p] > 0:
            minValue = min(minValue,nulcleaData["A"])
        elif sumC[q+1] - sumC[p] > 0:
            minValue = min(minValue,nulcleaData["C"])
        elif sumG[q+1] - sumG[p] > 0:
            minValue = min(minValue,nulcleaData["G"])
        elif sumT[q+1] - sumT[p] > 0:
            minValue = min(minValue,nulcleaData["T"])
        
        answers.append(minValue)  
        # print(minValue)  
        minValue = 5


    return answers


solution("CAGCCTA",[2,5,0],[4,5,6])












# def solution(S, P, Q):

#     M = {"A":1,
#         "C":2,
#         "G":3,
#         "T":4}
    
#     # sumA = [0]; sumC = [0]; sumG = [0]; sumT = [0]
#     # for nuke in S:
        
#     #     for sum in (sumA, sumC, sumG, sumT):
#     #         sum.append(sum[-1])
        
#     #     if nuke == 'A':
#     #         sumA[-1] += 1
#     #     elif nuke == 'C':
#     #         sumC[-1] += 1
#     #     elif nuke == 'G':
#     #         sumG[-1] += 1
#     #     else:
#     #         sumT[-1] += 1

#     sumA,sumC,sumG,sumT = [0],[0],[0],[0]

#     for i in S:
#         if i == "A":
#             sumA.append(M["A"])
#             sumC.append(0)
#             sumG.append(0)
#             sumT.append(0)
#         elif i == "C":
#             sumC.append(M["C"])
#             sumA.append(0)
#             sumG.append(0)
#             sumT.append(0)
#         elif i == "G":
#             sumG.append(M["G"])
#             sumC.append(0)
#             sumA.append(0)
#             sumT.append(0)
#         elif i == "T":
#             sumT.append(M["T"])
#             sumC.append(0)
#             sumG.append(0)
#             sumA.append(0)

#     for i in range(1,len(sumA)):
#         sumA[i]+=sumA[i-1]
#         sumC[i]+=sumC[i-1]
#         sumG[i]+=sumG[i-1]
#         sumT[i]+=sumT[i-1]
#     impact = []
#     for p, q in zip(P, Q):
#         if sumA[q+1] > sumA[p]:
#             impact.append(M['A'])
#         elif sumC[q+1] > sumC[p]:
#             impact.append(M['C'])
#         elif sumG[q + 1] > sumG[p]:
#             impact.append(M['G'])
#         else:
#             impact.append(M['T'])
#     return impact



# print(solution("CAGCCTA",[2,5,0],[4,5,6]))