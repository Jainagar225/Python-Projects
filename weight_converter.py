#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (Kg or Lbs): ")

if unit == "Kg":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is : {round(weight, 2)} {unit}")

elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is : {round(weight, 2)} {unit}")

else:
    print(f"{unit} was not valid")

