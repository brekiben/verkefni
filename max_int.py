#Við fáum inntak af jákvæðri heillri tölu
#Svo fáum við fleiri inntök 
#þanngað til við fáum inn neikvætt inntak
#þá á programmið að finna hæstu jákvæðu töluna af þeim sem við fengum inn


num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while num_int >= 0:
    num_int = int(input("Input a number: ")) 
    if num_int > max_int:
        max_int = num_int


print("The maximum is", max_int)    # Do not change this line
