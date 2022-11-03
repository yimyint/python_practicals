def main():
    #calculate bmi according to individual weight
    for weight in range(50,101,2):
         bmi = calculate_bmi(1.75, weight)
         category = determine_weight_category(bmi)
         print(f"Height {1.75}m, Weight {weight}kg = BMI {bmi:,.1f}, considered {category}")

    for height in range(150,200,10):
        for weight in range(50,101,10):
             bmi = calculate_bmi(height/100, weight)
             category = determine_weight_category(bmi)
             print(f"Height {height/100}m, Weight {weight}kg = BMI {bmi:,.1f}, considered {category}")

def calculate_bmi(height, weight):
    return weight / (height ** 2)

def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

main()
