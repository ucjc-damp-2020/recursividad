
lista= [1,1,1,1,1]

def sumatorio(list):
    res = 0
    for i in lista:
        res+=i
    return res


def sumatorio_rec(list, longitud):
    acum = 0
    if longitud>1:
        index = longitud-1
        acum = sumatorio_rec(list,index)
    return list[longitud-1] + acum


























