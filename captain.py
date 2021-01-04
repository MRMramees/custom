k=int(input("enter the number"))
if (k>1 and k<1000):
    a=input("enter the room number")
    list1=a.split(" ") 
    print(list1)
    for i in list1:   
        count= list1.count(i)
        if (count!=k):
            print (i)



#1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 