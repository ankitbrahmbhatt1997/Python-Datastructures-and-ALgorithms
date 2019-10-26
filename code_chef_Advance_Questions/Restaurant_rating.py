from sys import stdin
from heapq import heappush,heappop

def manage_top_reviews(top_reviews,remaining_reviews,x):
    if len(remaining_reviews) == 0:
        heappush(remaining_reviews,-x)
    else:
        top_count = (len(top_reviews) + len(remaining_reviews) + 1)//3
        
        if top_count > 0 :
            if len(top_reviews) == 0:
                heappush(remaining_reviews,-x)
                heappush(top_reviews,-heappop(remaining_reviews))
            else:
                if len(top_reviews) == top_count:
                    
                    if top_reviews[0] < x:
                        
                        heappush(remaining_reviews,-heappop(top_reviews))
                        heappush(top_reviews,x)
                    else:
                        heappush(remaining_reviews,-x)
                elif len(top_reviews) < top_count:
                    heappush(remaining_reviews,-x)
                    heappush(top_reviews,-heappop(remaining_reviews))
        elif top_count == 0:
            heappush(remaining_reviews,-x)

        

    

N = int(stdin.readline())
#min heap
top_reviews=[]
#max heap
remaining_reviews=[]

for _ in range(N):
    query = list(map(int,stdin.readline().strip().split(" ")))
    if len(query) == 2:
        query_type = query[0]
        x=query[1]
    else :
        query_type = 2

    if query_type == 1:
        manage_top_reviews(top_reviews,remaining_reviews,x)
        
    elif query_type == 2:
        
        if len(top_reviews) == 0:
            print("No reviews yet")
        else:
            print(top_reviews[0])
    
    
    


