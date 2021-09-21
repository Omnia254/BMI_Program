# how to calculate BMI
def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi
 
# input height and weight
height=float(input("\n Enter your height in m : "))
weight=float(input("\n Enter your weight in kg : "))
 
# call the BMI function
bmi = BMI(height, weight)
print("\n The BMI is", format(bmi), "so ", end='')
 
# Conditions to find out BMI 
if (bmi < 18.5):
    print("underweight")
 
elif ( bmi >= 18.5 and bmi < 24.9):
    print("Healthy")
 
elif ( bmi >= 24.9 and bmi < 30):
    print("overweight")
 
elif ( bmi >=30):
    print("Obesity")
elif ( bmi >= 40):
    print("Morbid Obesity")






