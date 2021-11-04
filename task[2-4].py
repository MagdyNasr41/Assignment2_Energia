#input = 3 ,6 , 24
def snake (n):
    counter = 0
    sum = 1
    while sum < n*n - sum:
        sum = sum*2
        counter += 1
#        print(f"{counter} - {sum} - {n*n - sum}\n")
    return counter 
print(snake(24))
    