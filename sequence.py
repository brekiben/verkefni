#við fáum inntak sem tilgreinir um hversu oft við eigum að prenta
#Við þurfum svo að gera programm sem tekur sýnir summu seinustu 3 tölurnar
#

n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter = 0
holder1 = 1
holder2 = 2
holder3 = 3
while counter < n:
    if counter==0:
       print(holder1)
    elif counter==1:
        print(holder2)
    elif counter==2:
        print(holder3)
    else:
        nytala=holder1+holder2+holder3
        print(nytala)
        holder1=holder2
        holder2=holder3
        holder3=nytala
    counter += 1


        

    
    