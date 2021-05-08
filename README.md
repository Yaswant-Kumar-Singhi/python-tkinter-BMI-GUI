# python-tkinter-BMI-GUI
>Create a BMI Calculator using tkinter using python

> Steps for BMI Calculation
```
1. Enter WEIGHT from user
2. Enter HEIGHT from user in meters
3. BMI = WEIGHT / (HEIGHT ** 2)
4. Print BMI

```

>Understand how BMI Calculator works

```
STEP 1 : Goto bmi.py to get the python script for calculating BMI for an individual.

bmi.py

print('This program is used to calculate BMI of an individual \n')
name   = input("Enter your name")
weight = float(input("Enter your weight"))
height = float(input("Enter your height"))

ht_in_m = (height * 0.3048)
ht_cal = ht_in_m **2 


bmi = weight / ht_cal

print(f"{name} your BMI is {bmi}")

```
> GUI for BMI Calculator
<img src="https://github.com/Yaswant-Kumar-Singhi/python-tkinter-BMI-GUI/blob/main/BMI%20Calculator.PNG">

```
1. This GUI is divided into grid system of ros of columns 
2. No of rows = 3 {0,1,2}
3. No of Columns = 2 {0,1}
4. padding of 5units is also done in every cell
5. In total there are 6 cells
6. BMI will be rounded upto 3 decimal points
7. Sample test file is given below
```

<img src="https://github.com/Yaswant-Kumar-Singhi/python-tkinter-BMI-GUI/blob/main/BMI_Sample_run_image.PNG">

