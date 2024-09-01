height = float(input("What is your height in centimeters: ")) 
weight = float(input("What is your weight in kilograms: ")) 

height_meters = height / 100
bmi = weight / (height*height)

print(f"Your bmi is {bmi: .2f}")
