def quickSort(liste,baslangic,bitis):
    if bitis<baslangic:
        return
    pivotIndisi=bolme(liste,baslangic,bitis)
    quickSort(liste,baslangic,pivotIndisi-1)
    quickSort(liste,pivotIndisi+1,bitis)
def bolme(liste,baslangic,bitis):
    pivot=liste[bitis]
    i=baslangic-1
    for j in range(baslangic,bitis):
        if liste[j]<=pivot:
            i+=1
            liste[i],liste[j]=liste[j],liste[i]
    liste[i+1],liste[bitis]=liste[bitis],liste[i+1]
    return i+1
def listeyiYaz(liste):
    for i in range (len(liste)):
        print(liste[i],end=" ")
liste=([13,22,53,17,5,-22,3])
quickSort(liste,0,len(liste)-1)
listeyiYaz(liste)