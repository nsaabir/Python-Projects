#Nile Saabir
#6-26-17
#Lab 5
#Hillary Fleenor

#Prompt for a speed limit and clocked speed
print("Welcome to the speed fine calculator!")

limit_speed = float(input("Enter the speed limit :"))
clocked_speed = float(input("Enter the clocked speed :"))
diff=(clocked_speed-limit_speed)*5
fine=diff+50
Above_90 = fine + 90 

if clocked_speed < limit_speed:
    print(" No Fine :")

elif clocked_speed > limit_speed and clocked_speed<90:
    
    print("Fine :",fine)

elif clocked_speed > 90:
     print("Fine :",Above_90)
    
else:
    print("Speed is legal")
