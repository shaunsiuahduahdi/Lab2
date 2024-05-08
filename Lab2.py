print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
        print ("Enter some numbers separated by commas (e.g. 5, 67, 32)")



def get_user_input():
   y = input()
   numlist=y.split(",")
   numlist=[float(y) for y in numlist]
   print (numlist)

   return numlist

def calc_average_temperature(numlist):
     average = sum(numlist)/len(numlist)
     print(average)
     return average

def calc_min_max_temperature(numlist):
    min_max = [min(numlist), max(numlist)]
    print(min_max)
    return min_max
    
    

display_main_menu()
numlist = get_user_input()
calc_average_temperature(numlist)
calc_min_max_temperature(numlist)
