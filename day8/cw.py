1. #შექმენი ორი Boolean ცვლადი: `is_student` და `is_teacher`. შეინახე მათში `True` და `False` მნიშვნელობები და დაბეჭდე ორივე ცვლადი.
2. #მომხმარებელს შეაყვანინე ასაკი და შეამოწმე, არის თუ არა ის 18 წლის ან მეტი. დაბეჭდე მიღებული `True` ან `False` შედეგი.
3. #შექმენი ორი Boolean ცვლადი: `has_ticket` და `has_id`. გამოიყენე `and` და შეამოწმე, აქვს თუ არა ადამიანს ორივე.
4. #შექმენი ორი Boolean ცვლადი: `has_money` და `has_card`. გამოიყენე `or` და შეამოწმე, აქვს თუ არა ადამიანს ფულის გადახდის საშუალება.
5. #შექმენი Boolean ცვლადი `is_raining = False`. გამოიყენე `not` და დაბეჭდე მისი საპირისპირო მნიშვნელობა


#1)
is_student = True
is_teacher = False

print(is_student)
print(is_teacher)

#2)
age = int(input("enter your age: "))
is_adult = age >= 18
print(is_adult)

#3)
has_ticket = True
has_id = False

can_enter = has_ticket and has_id
print(can_enter)

#4)
has_money = False
has_card = True
can_pay = has_money or has_card
print(can_pay)

#5)
is_raining = False
is_sunny = not is_raining
print(is_sunny)








