def bubbleSort(Lista):
    for i in range(0,len(Lista)-1):
        for j in range(0,len(Lista)-1-i):
            if(Lista[j]>Lista[j+1]):
                Lista[j],Lista[j+1]=Lista[j+1],Lista[j]
    return Lista
ListaTeste=[4,2,6,3]
print(bubbleSort(ListaTeste))
