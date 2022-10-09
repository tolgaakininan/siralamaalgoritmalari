def bubbleSort(liste):
    uzunluk=len(liste)
    for i in range(uzunluk-1):
        for j in range (uzunluk-1-i):
            if liste[j]>liste[j+1]:
               liste[j],liste[j+1]=liste[j+1],liste[j]
def listeyiYaz(liste):
    for i in range (len(liste)):
        print(liste[i],end=" ")
liste=([13,22,53,17,5,-22,3])
bubbleSort(liste)
listeyiYaz(liste)