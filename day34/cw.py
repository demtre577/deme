
# 1) შექმენი ორი Set სახელად `fruits1` და `fruits2`. პირველში შეინახე 5 ხილი, ხოლო მეორეში 5 ხილი. 
# გამოიყენე `union()` მეთოდი, რათა მიიღო ორივე Set-ის ყველა უნიკალური ხილი და დაბეჭდე მიღებული შედეგი.

# 2) შექმენი ორი Set სახელად `numbers1` და `numbers2`. პირველში შეინახე რიცხვები `{10, 20, 30,
#                                                                                   40, 50}`, ხოლო მეორეში
# `{30, 40, 50, 60, 70}`. გამოიყენე `intersection()` მეთოდი და დაბეჭდე მხოლოდ ის რიცხვები, რომლებიც ორივე Set-ში გვხვდება.

# 3) შექმენი ორი Set სახელად `students1` და `students2`. პირველში შეინახე 4 მოსწავლის სახელი,
# ხოლო მეორეში  4 მოსწავლის სახელი. გამოიყენე `union()` მეთოდი, რათა მიიღო ყველა უნიკალური მოსწავლის სახელი.
# შემდეგ გამოიყენე `len()` ფუნქცია და დაბეჭდე მიღებულ Set-ში არსებული მოსწავლეების რაოდენობა.

# 4) შექმენი ორი Set სახელად `colors1` და `colors2`. პირველში შეინახე ფერები: `red`, `green`, 
# `blue`, `yellow`, ხოლო მეორეში  `blue`, `yellow`, `black`, `white`. გამოიყენე `intersection()` მეთოდი, რათა გაიგო,
# რომელი ფერები მეორდება ორივე Set-ში. მიღებული შედეგი დაბეჭდე ეკრანზე.

# 5) შექმენი სამი Set სახელად `python_students`, `javascript_students` და `react_students`.
# თითოეულში შეინახე იმ მოსწავლეების სახელები, რომლებიც შესაბამის ტექნოლოგიას სწავლობენ. გამოიყენე `union()` მეთოდი,
# რათა მიიღო ყველა უნიკალური მოსწავლის სახელი. შემდეგ გამოიყენე `intersection()` მეთოდი `python_students` და 
# `javascript_students` Set-ებზე, რათა იპოვo
# მოსწავლეები, რომლებიც ორივე ტექნოლოგიას სწავლობენ. ორივე შედეგი დაბეჭდე ეკრანზე




#1)
fruits1 = {"apple", "banana", "orange", "peach", "strawberry"}
fruits2 = {"pear", "banana", "kiwi", "peach", "cherry"}
all_fruits = fruits1.union(fruits2)
print(all_fruits)




#2)
numbers1 = {10, 20, 30, 40, 50}
numbers2 = {30, 40, 50, 60, 70}
common_numbers = numbers1.intersection(numbers2)
print(common_numbers)


#3)
students1 = {"გიორგი", "ანი", "ლუკა", "მარიამი"}
students2 = {"დავითი", "ანი", "ნიკოლოზი", "ლუკა"}
all_students = students1.union(students2)
students_count = len(all_students)
print(f"უნიკალური მოსწავლეების რაოდენობა: {students_count}")


#4)
colors1 = {"red", "green", "blue", "yellow"}
colors2 = {"blue", "yellow", "black", "white"}
common_colors = colors1.intersection(colors2)
print(common_colors)




#5)
python_students = {"Nika", "Luka", "Giorgi", "Mariam"}
javascript_students = {"Ani", "Luka", "Daviti", "Giorgi"}
react_students = {"Mariam", "Nikolozi", "Ani"}
all_students = python_students.union(javascript_students, react_students)
both_python_js = python_students.intersection(javascript_students)
print(f"All unique students: {all_students}")
print(f"Students studying both Python and JS: {both_python_js}")















































