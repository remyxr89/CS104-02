#CS104
#Xochitl Martinez
#conditions.py
i = 1
while i <= 1:
    temp = int (input("please enter the current temperature: "))
    if temp >= 90:
        print("wear shorts")
    elif (temp >= 70):
        print("short sleeves are fine")
    elif (temp >= 50):
        print("wear a jacket")
    elif (temp >= 32):
        print("wear a heavy coat")
    else:
         print("stay inside")
