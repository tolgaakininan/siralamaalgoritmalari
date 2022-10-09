def selectionSort(liste):
    for i in range(len(liste)):
        minimumIndis=i
        for j in range(i+1,len(liste)):
            if(liste[minimumIndis]>liste[j]):
                minimumIndis=j
        liste[i],liste[minimumIndis]=liste[minimumIndis],liste[i]
def listeyiYaz(liste):
    for i in range (len(liste)):
        print(liste[i],end=" ")
liste=([13,22,53,17,5,-22,3])
selectionSort(liste)
listeyiYaz(liste)