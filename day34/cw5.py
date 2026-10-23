python_students = {"Nika", "Luka", "Giorgi", "Mariam"}
javascript_students = {"Ani", "Luka", "Daviti", "Giorgi"}
react_students = {"Mariam", "Nikolozi", "Ani"}
all_students = python_students.union(javascript_students, react_students)
both_python_js = python_students.intersection(javascript_students)
print(f"All unique students: {all_students}")
print(f"Students studying both Python and JS: {both_python_js}")