print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
        print ("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
   y = input()
   numlist=y.split(",")
   numlist=[float(y) for y in numlist]
   
   print (numlist)

   return numlist

def calc_average_temperature():

    
    temp_sum=sum(temp_list)
    temp_count=len(temp_list)
    temp_avg=temp_sum/temp_count
    print(temp_avg)
    return(temp_avg)



def calc_min_max_temperature():
    tempMin = float('inf')
    for numm in temp_list:
        if (numm < tempMin):
            tempMin = int(numm)
    
    tempMax = float('-inf')
    for nummm in temp_list:
        if (nummm > tempMax):
            tempMax = int(nummm)
    print("Minimum Temp is: " + str(tempMin))
    print("Maximum Temp is: " + str(tempMax))
    return(tempMin, tempMax)

display_main_menu()
temp_list=get_user_input()
calc_average_temperature()          
calc_min_max_temperature()


