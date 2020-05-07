def can_place_flags(peaks, flags_to_place):
    current_position = 1 - flags_to_place
    for i in range(flags_to_place):
        if current_position + flags_to_place > len(peaks) - 1:
            return False
        current_position = peaks[current_position + flags_to_place]
    return current_position < len(peaks)




def solution(A):
    peakCount = 0
    peaksList = []
    currentPeak = len(A)
    peaksList.insert(0,currentPeak)
    for i in range(len(A)-2,0,-1):
        if A[i-1] < A[i] > A[i+1]:
            peakCount+=1
            currentPeak = i
        
        peaksList.insert(0,currentPeak)
    
    peaksList.insert(0,currentPeak)

    current_guess = 0
    next_guess = 0
    while can_place_flags(peaksList, next_guess):
        current_guess = next_guess
        next_guess += 1
    return current_guess

        



    

    
        
    # return len(allowed)




print(solution([1,5,3,4,3,4,1,2,3,5,6,2]))

