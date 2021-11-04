# 7 , 5 
var = 7
factor = 5
def listato (var , factor):
    l = []
    a = 1
    while len(l) < factor:
        l.append(var*a)
        a += 1
    return l
    
l = listato(7 , 5)
print(l)