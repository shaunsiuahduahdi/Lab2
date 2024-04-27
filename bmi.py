def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height*height)

    print ("BMI =" + str(bmi))


    if (bmi < 18.5):
        print ("Underweight")

    elif(18.5<bmi<25):
        print ("Acceptable")

    else:
        print ("lose some weight")
    
calculate_bmi(weight=100, height=1.30)