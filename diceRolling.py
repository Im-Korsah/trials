import random
import time


ans = "yes"
   
while ans == "yes" or ans == "Yes":
    time.sleep(1)
    value = random.randint(1,6)
    print(value)
    

    if value == 6:
        print("you have won")
    else:
        print("you have lost")



    ans = input("\n Do You want to play Again Yes/NO \n")


