
import tkinter

root = tkinter.Tk()
root.geometry("200x100")
root.title("BMI Calculator")

# create functions
def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round((kg / (height ** 2)),3)
    print(round(bmi,2))
    lable_result['text'] = f"BMI : {bmi}"

# create GUI

lable_kg = tkinter.Label(root, text="KG : ")
lable_kg.grid(column=0, row=0, padx=5, pady=5)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=1, row=0 , padx=5, pady=5)


lable_height = tkinter.Label(root, text="Height : ")
lable_height.grid(column=0, row=1, padx=5, pady=5)


entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1, padx=5, pady=5)

lable_result = tkinter.Label(root, text="BMI : ")
lable_result.grid(column=1, row=2, padx=5, pady=5)

button_calculate = tkinter.Button(root, text = "Calculate" , command=calculate_bmi)
button_calculate.grid(column=0, row=2, padx=5, pady=5)




root.mainloop()
