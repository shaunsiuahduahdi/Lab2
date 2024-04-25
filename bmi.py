def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height*height)

    print ("BMI =" + str(bmi))


    if (bmi > 18.5):
        print ("Overweight")

calculate_bmi(weight=58, height=1.64)