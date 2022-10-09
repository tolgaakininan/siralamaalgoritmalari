def insertionSort(liste):
    for i in range(len(liste)):
        anahtar=liste[i]
        j=i-1
        while j>=0 and liste[j]>anahtar:
            liste[j+1],liste[j]=liste[j],liste[j+1]
            j-=1
        liste[j+1]=anahtar
def listeyiYaz(liste):
    for i in range (len(liste)):
        print(liste[i],end=" ")
liste=([13,22,53,17,5,-22,3])
insertionSort(liste)
listeyiYaz(liste)