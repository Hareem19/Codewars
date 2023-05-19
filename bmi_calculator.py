def bmi_fn(weight, height):
    #your code here
    bmi=weight/(height*height)
    print(bmi)
    if bmi <= 18.5 :
        return "Underweight"
    elif 18.5 < bmi <= 25.0:
        return "Normal"
    elif 25.0 < bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
print(bmi_fn(7000,7))
#     Write
#     function
#     bmi
#     that
#     calculates
#     body
#     mass
#     index(bmi=weight / height2).
#
#     if bmi <= 18.5 return "Underweight"
#
#     if bmi <= 25.0 return "Normal"
#
#     if bmi <= 30.0 return "Overweight"
#
#     if bmi > 30 return "Obese"
#
