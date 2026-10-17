# 1) შექმენი Tuple სახელად colors, რომელშიც იქნება 4 ფერი: "red", "green", "blue", "yellow".
# დაბეჭდე პირველი და ბოლო ელემენტი.

# 2) შექმენი Tuple რიცხვებით: (10, 20, 30, 40, 50, 60).
# დაბეჭდე Tuple-ის სიგრძე (len() ფუნქციის გამოყენებით).

# 3)შექმენი 3-ელემენტიანი Tuple:  point = (10, 20, 30).
# მიანიჭე ეს მნიშვნელობები სამ ცვლადს (x, y, z) Unpacking-ის საშუალებით და დაბეჭდე თითოეული ცვლადი

# 4) ექმენი Tuple სახელად user_info = ("გიორგი", 25, "თბილისი").
# Unpacking-ით მიანიჭე ეს მნიშვნელობები ცვლადებს: name, age, city.
# დაბეჭდე თითოეული ცვლადი ცალ-ცალკე.

# 5) მოცემულია Tuple: numbers = (1, 5, 3, 5, 2, 5, 8, 4).
# დაითვალე, რამდენჯერ გვხვდება რიცხვი 5 (.count() მეთოდით).
# იპოვე, რომელ ინდექსზე დგას პირველად რიცხვი 3 (.index() მეთოდით).



#1)
colors = ("red", "green", "blue", "yellow")
print("First element:", colors[0])
print("Last element:", colors[-1])


#2)
numbers = (10, 20, 30, 40, 50, 60)
print("Length of the tuple:", len(numbers))

#3)
point = (10, 20, 30)
x, y, z = point
print("x:", x)
print("y:", y)
print("z:", z



#4)
user_info = ("გიორგი", 25, "თბილისი")
name, age, city = user_info
print("Name:", name)
print("Age:", age)
print("City:", city)




numbers = (1, 5, 3, 5, 2, 5, 8, 4)
count_of_five = numbers.count(5)
index_of_three = numbers.index(3)
print("The number 5 appears:", count_of_five, "times")
print("The first index of 3 is:", index_of_three)