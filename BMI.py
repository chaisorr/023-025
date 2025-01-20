def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI).

    Parameters:
    weight (float): Weight in kilograms.
    height (float): Height in meters.

    Returns:
    float: BMI value.
    """
    # Calculate BMI using the formula: BMI = weight / (height ** 2)
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    """
    Categorize the BMI value based on the given ranges.

    Parameters:
    bmi (float): The BMI value.

    Returns:
    str: The BMI category description in Thai.
    """
    if bmi < 18.50:
        return "น้ำหนักน้อย / ผอม (มากกว่าคนปกติ)"
    elif 18.50 <= bmi <= 22.90:
        return "ปกติ (สุขภาพดี) (เท่าคนปกติ)"
    elif 23 <= bmi <= 24.90:
        return "ท้วม (โรคอ้วนระดับ 1)"
    elif 25 <= bmi <= 29.90:
        return "อ้วน (โรคอ้วนระดับ 2)"
    else:
        return "อ้วนมาก (โรคอ้วนระดับ 3)"

# Get user input for weight, height, and age
weight = float(input("Enter your weight in kilograms: "))  # Prompt user for weight input
height = float(input("Enter your height in meters: "))  # Prompt user for height input
age = int(input("Enter your age in years: "))  # Prompt user for age input (integer)

# Call the function to calculate BMI
bmi = calculate_bmi(weight, height)

# Call the function to categorize BMI
bmi_category = categorize_bmi(bmi)

# Print the result with 2 decimal places and display the age and category
print(f"Your age is: {age} years")
print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {bmi_category}")
