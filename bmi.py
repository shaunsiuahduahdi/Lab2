def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height*height)

    print ("BMI =" + str(bmi))


    if (bmi < 18.5):
        print ("Underweight")  
        return(-1)

    elif(18.5<bmi<25):
        print ("Acceptable")
        return(0)
    else:
        print ("lose some weight")
        return(1)
    
calculate_bmi(weight=100, height=1.30)