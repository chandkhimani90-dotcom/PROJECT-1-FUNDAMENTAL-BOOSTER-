# ===============================================
# Name: __________________
# Roll No: _______________
# Project: Fundamental Booster
# Interactive Personal Data Collector
# ===============================================

print("=" * 60)
print("        FUNDAMENTAL BOOSTER PROJECT")
print("      INTERACTIVE PERSONAL DATA COLLECTOR")
print("=" * 60)

print("\nPlease enter your personal details.\n")

# ---------- Taking Input ----------
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
height = float(input("Enter Your Height (in cm): "))
fav_num = int(input("Enter Your Favourite Number: "))

# ---------- Calculations ----------
current_year = 2026
birth_year = current_year - age

height_meter = height / 100
height_int = int(height)

double = fav_num * 2
half = fav_num / 2
square = fav_num ** 2
sum_value = fav_num + age
difference = fav_num - age

# ---------- Display Information ----------
print("\n" + "=" * 60)
print("               PERSONAL INFORMATION")
print("=" * 60)

print("Name               :", name)
print("Age                :", age, "Years")
print("Height             :", height, "cm")
print("Favourite Number   :", fav_num)

print("\n" + "-" * 60)
print("CALCULATED INFORMATION")
print("-" * 60)

print("Estimated Birth Year :", birth_year)
print("Height in Meter      :", round(height_meter, 2), "m")
print("Double Number        :", double)
print("Half Number          :", half)
print("Square Number        :", square)
print("Age + Favourite No.  :", sum_value)
print("Age - Favourite No.  :", difference)

# ---------- Type Casting ----------
print("\n" + "-" * 60)
print("TYPE CASTING")
print("-" * 60)

print("Original Height (Float) :", height)
print("Converted Height (Int)  :", height_int)
print("Age as Float            :", float(age))

# ---------- Type & ID ----------
print("\n" + "=" * 60)
print("VARIABLE DETAILS")
print("=" * 60)

print("\nVariable : name")
print("Value    :", name)
print("Type     :", type(name))
print("Memory ID:", id(name))

print("\nVariable : age")
print("Value    :", age)
print("Type     :", type(age))
print("Memory ID:", id(age))

print("\nVariable : height")
print("Value    :", height)
print("Type     :", type(height))
print("Memory ID:", id(height))

print("\nVariable : fav_num")
print("Value    :", fav_num)
print("Type     :", type(fav_num))
print("Memory ID:", id(fav_num))

print("\nVariable : birth_year")
print("Value    :", birth_year)
print("Type     :", type(birth_year))
print("Memory ID:", id(birth_year))

# ---------- Project Summary ----------
print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print("Hello,", name)
print("Thank you for using the Interactive Personal Data Collector.")
print("Your data has been collected and processed successfully.")
print("This project demonstrates:")
print("1. print() function")
print("2. input() function")
print("3. Variables")
print("4. Data Types")
print("5. Arithmetic Operators")
print("6. Type Casting")
print("7. type() Function")
print("8. id() Function")


print("\n" + "=" * 60)
print("Project Completed Successfully!")
print("Thank You, GIRISH SIR, for your guidance and support.")
print("Have a Nice Day!")
print("=" * 60)




