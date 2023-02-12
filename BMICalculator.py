# Calculate BMI: BMI = weight/height^2
# Code is self-explanatory
def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        output = 'Underweight'
    elif bmi <= 25:
        output = 'Normal'
    elif bmi <= 30:
        output = 'Overweight'
    else:
        output = 'Obese'
    return output
