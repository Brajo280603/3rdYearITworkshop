def add_student(grades_dict, name, grades):
    grades_dict[name] = grades

def calculate_average(grades):
    return sum(grades) / len(grades)

def find_top_student(grades_dict):
    top_student = None
    highest_avg = 0
    for student, grades in grades_dict.items():
        avg = calculate_average(grades)
        if avg > highest_avg:
            highest_avg = avg
            top_student = student
    return top_student, highest_avg

grades_dict = {}
add_student(grades_dict, 'Alice', [85, 90, 92])
add_student(grades_dict, 'Bob', [78, 82, 80])
add_student(grades_dict, 'Charlie', [95, 90, 98])

for student, grades in grades_dict.items():
    print(f"{student}: {calculate_average(grades):.2f}")

top_student, highest_avg = find_top_student(grades_dict)
print(f"Top Student: {top_student} with an average of {highest_avg:.2f}")