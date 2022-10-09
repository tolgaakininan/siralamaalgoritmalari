def countingSort(liste,min,max):
    countArr=[0]*(max-min+1)
    for i in liste:
        countArr[i-min]+=1
    j=0
    for i in range(min,max+1):
        if countArr[i-min]>0:
            liste[j]=i
            countArr[i-min]-=1
            j+=1
def listeyiYaz(liste):
    for i in range (len(liste)):
        print(liste[i],end=" ")
liste=([9,1,3,5,2,7,8,6,4])
countingSort(liste,1,9)
listeyiYaz(liste)