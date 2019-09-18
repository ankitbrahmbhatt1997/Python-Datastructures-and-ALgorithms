def threeNumberSum(array, targetSum):
    array.sort()
    result=[]
    
    for i in range(len(array)):
        left = i+1
        right = len(array)-1
        print("       ")
        print("for i  = ",i,"and value =",array[i])
        print("------------")
        while left < right:
            
            comb = array[left] + array[right]
            
            target = targetSum - comb
            print("indexes are",[i,left,right])
            print("values are",[array[i],array[left],array[right]])
            
            if target == array[i]:
                print("ok")
                result.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif target > array[i]:
                left+=1
            elif target < array[i]:
                right-=1

    return result

print(threeNumberSum([12,3,1,2,-6,5,0,-8,-1,6,-5],0))