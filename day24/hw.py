# 1. შექმენი List, რომელშიც იქნება 5 სხვადასხვა სასმელი:

# - Water
# - Milk
# - Tea
# - Coffee
# - Juice

# გამოიტანე List კონსოლში.


# 2. მოცემულია:

# countries = ["Georgia", "USA", "Germany", "France", "Japan"]

# ინდექსების გამოყენებით გამოიტანე:
# - მეორე ელემენტი.
# - მეოთხე ელემენტი.
# - ბოლო ელემენტი (უარყოფითი ინდექსით).


# 3. შექმენი List, რომელშიც იქნება 5 სხვადასხვა სპორტის სახეობა.

#ინდექსის გამოყენებით შეცვალე მესამე ელემენტი სხვა სპორტით.

#გამოიტანე განახლებული List.


# 4. მოცემულია:

# prices = [15, 25, 35, 45, 55]

# ინდექსების გამოყენებით შეცვალე:
# - პირველი ელემენტი რიცხვით 10.
# - ბოლოსწინა ელემენტი რიცხვით 40.

# გამოიტანე განახლებული List.


# 5. მოცემულია:

# movies = ["Inception", "Matrix", "Avatar", "Titanic", "Gladiator"]

# Slicing-ის გამოყენებით გამოიტანე:
# - პირველი სამი ფილმი.
# - ბოლო ორი ფილმი.
# - მეორე ფილმიდან მეოთხე ფილმამდე.


# 6. შექმენი List, რომელშიც იქნება 5 სკოლის საგანი.

# Slicing-ის გამოყენებით გამოიტანე პირველი 2 საგანი.


# 7. მოცემულია:

# letters = ["A", "B", "C", "D", "E", "F"]

# Slicing-ის გამოყენებით გამოიტანე მხოლოდ შუა 4 ასო.


# 8. მოცემულია:

# numbers = [5, 10, 15, 20, 25, 30, 35, 40]

# Slicing-ის ნაბიჯის ([::step]) გამოყენებით გამოიტანე ყოველი მეორე რიცხვი.


# 9. შექმენი List, რომელშიც იქნება 5 სხვადასხვა სახელი.

# Slicing-ის ([::-1]) გამოყენებით ამოატრიალე სია უკუღმა და გამოიტანე შედეგი.


# 10. მოცემულია:

# items = ["Book", "Pen", "Pencil", "Eraser", "Ruler"]

# ინდექსების გამოყენებით შეცვალე პირველი და ბოლო ელემენტი ახალი ნივთებით და გამოიტანე განახლებული List.





#1.
drinks = ["Water", "Milk", "Tea", "Coffee", "Juice"]
print(drinks)



#2.
countries = ["Georgia", "USA", "Germany", "France", "Japan"]
print(countries[1])
print(countries[3])
print(countries[-1])



#3.
sports = ["Football", "Basketball", "Tennis", "Rugby", "Swimming"]
sports[2] = "Volleyball"
print(sports)


#4.
prices = [15, 25, 35, 45, 55]
prices[0] = 10
prices[-2] = 40


#5.
movies = ["Inception", "Matrix", "Avatar", "Titanic", "Gladiadiator"]
print(movies[:3])
print(movies[-2:])
print(movies[1:4])


#6.
subjects = ["მათემატიკა", "ქართული", "ისტორია", "ფიზიკა", "ინგლისური"]
first_two = subjects[0:2]
print(first_two)


#7.
letters = ["A", "B", "C", "D", "E", "F"]
middle_four = letters[1:5]
print(middle_four)


#8.
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
every_second = numbers[::2]
print(every_second)


#9.
names = ["გიორგი", "ნიკა", "ანა", "ლუკა", "მარიამი"]
reversed_names = names[::-1]
print(reversed_names)


#10.
items = ["Book", "Pen", "Pencil", "Eraser", "Ruler"]
items[0] = "Notebook"
items[-1] = "Marker"
print(items)