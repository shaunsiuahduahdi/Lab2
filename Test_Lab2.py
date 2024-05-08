import Lab2 as lab2

print("Lab2_Testing")

def test_average():
   average = lab2.calc_average_temperature(6.0, 7.0)
   assert (average == 6.5)

def test_min_max():
   min_max = lab2.calc_min_max_temperature(6.0, 7.0)
   assert (min_max[0] == 6.0 and min_max[1] ==7.0)