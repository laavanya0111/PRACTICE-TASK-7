n = int(input("Enter how many elements you want to enter"))
els = print("Enter Elements: ")
list1 = list(els)
print(list1)
for(i in range(1,n)):
    for(j in range(1,n-i)):
        if(list[j]>list[j+1]):
            (list[j],list[j+1]) = (list[j+1],list[j])
print("Sorted List are:",list(els))            