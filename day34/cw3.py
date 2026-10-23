students1 = {"გიორგი", "ანი", "ლუკა", "მარიამი"}
students2 = {"დავითი", "ანი", "ნიკოლოზი", "ლუკა"}
all_students = students1.union(students2)
students_count = len(all_students)
print(f"უნიკალური მოსწავლეების რაოდენობა: {students_count}")