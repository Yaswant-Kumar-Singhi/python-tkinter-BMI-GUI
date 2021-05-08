

print('This program is used to calculate BMI of an individual \n')
name   = input("Enter your name")
weight = float(input("Enter your weight"))
height = float(input("Enter your height"))

ht_in_m = (height * 0.3048)
ht_cal = ht_in_m **2 


bmi = weight / ht_cal

print(f"{name} your BMI is {bmi}")
