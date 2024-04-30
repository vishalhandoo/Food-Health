# utils.py
def calculate_bmi(height, weight):
    height=height
    return weight / (height * height)

def calculate_daily_calories(bmi):
    BASE_CALORIES = 2000  
    BMI_MULTIPLIER = 10   
    BMI_THRESHOLD = 25    

    if bmi < BMI_THRESHOLD:
        calorie_adjustment = (BMI_THRESHOLD - bmi) * BMI_MULTIPLIER
        daily_calories = BASE_CALORIES - calorie_adjustment
    
    else:
        calorie_adjustment = (bmi - BMI_THRESHOLD) * BMI_MULTIPLIER
        daily_calories = BASE_CALORIES + calorie_adjustment

    return daily_calories
