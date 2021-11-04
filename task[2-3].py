#input = [1, 2, 3, 4, 5, 6]
#input = [-1, -2, -3, -4, -5, -6]
#input = [0, 0]

def sum (l):
    listato = []
    sumEven = 0
    sumOdd = 0
    for n in l:
        if n%2==0:
            sumEven += n
        else:
            sumOdd += n
    listato.append(sumEven)
    listato.append(sumOdd)
    return listato
            
print(sum([0, 0]))