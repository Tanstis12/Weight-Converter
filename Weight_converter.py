#Thomas Anstis
#02/11/2025
#Weight converter

weight = float(input("What is your weight?: "))
unit = input("Kilograms or Pounds (K/L): ")    

if unit == "K":
    weight *= 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is NOT a VALID UNIT!")

