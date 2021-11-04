l1 = [2,4,1]
l2 = [4,2,1]
#[1, 2, 3] , [1, 2, 4]
#[0, 1, 5] , [0, 1, 5]

def parallel (l1 , l2) :
    
    if -l1[0]/l1[1] == -l2[0]/l2[1]:
         print("The Two Lines Are Parallel.")
    else:
         print("The Two Lines Are Not Parallel.")
parallel(l1, l2)