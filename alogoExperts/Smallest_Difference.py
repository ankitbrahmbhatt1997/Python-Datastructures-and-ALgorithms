def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pair=[]
    absDifference = None
    i = 0 
    j = 0
    while i < len(arrayOne) and j < len(arrayTwo):
        
        if arrayOne[i] == arrayTwo[j]:
            pair=[arrayOne[i],arrayTwo[j]]
            break
        else:
            currentDifference = abs(arrayOne[i]-arrayTwo[j])
            if absDifference is None:
                absDifference = currentDifference
                pair=[arrayOne[i],arrayTwo[j]]
                

                  
            else:
                if currentDifference < absDifference:
                    absDifference = currentDifference
                    pair=[arrayOne[i],arrayTwo[j]]
               
            if arrayOne[i] < arrayTwo[j]:
                i+=1
            elif arrayOne[i] > arrayTwo[j]:
                j+=1

    return pair
    
       

print(smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17]))