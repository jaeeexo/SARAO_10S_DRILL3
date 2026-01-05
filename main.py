from pyscript import Element

def check_grade():
    # Get the input value
    grade_input = Element("grade").value
    result_box = Element("result").element

    # Check if input is empty
    if grade_input == "":
        result_box.innerHTML = "Please enter a grade."
    else:
        grade = int(grade_input)

        # Determine if the student passed or failed
        if grade >= 75:
            result_box.innerHTML = f"Grade: {grade}<br>Status: Passed ✅"
        else:
            result_box.innerHTML = f"Grade: {grade}<br>Status: Failed ❌"
