#1) მომხმარებელს შეაყვანინე ასაკი, გადააქციე  int-ად და დაბეჭდე შედეგი.

#2) მომხმარებელს შეაყვანინე ასაკი, გადააქციე int-ად, მიუმატე 10 და დაბეჭდე შედეგი.
მ
#3) მომხმარებელს შეაყვანინე ორი რიცხვი, ორივე გადააქციე int-ად და დაბეჭდე მათი ჯამი.

#4) მომხმარებელს შეაყვანინე სიმაღლე, გადააქციე float-ად და დაბეჭდე მისი ტიპი.

#5) მომხმარებელს შეაყვანინე პროდუქტის ფასი, გადააქციე float-ად, მიუმატე 5.5 და დაბეჭდე შედეგი.

#6) შექმენი ცვლადები name, age და height. დაბეჭდე თითოეულის ტიპი type-ის გამოყენებით.

#7) ომხმარებელს შეაყვანინე სახელი და ასაკი. ასაკი გადააქციე int-ად და f-string-ის გამოყენებით დაბეჭდე:
#hello Nika you are 15 years old

#8) მომხმარებელს შეაყვანინე ორი რიცხვი, ორივე გადააქციე int-ად და დაბეჭდე მათი ნამრავლი.

#9) მომხმარებელს შეაყვანინე საყვარელი რიცხვი, გადააქციე int -ად, გამოაკელი 3 და დაბეჭდე შედეგი.

#10) მომხმარებელს შეაყვანინე ასაკი, გადააქციე int-ად, შემდეგ დაბეჭდე:
#ასაკი
#ასაკს დამატებული 10 
#ასაკის ტიპი type-ის გამოყენებით

#1)
age=int("enter your age")
print(type(age))

#2)  
age=int("enter your age")
print(age + 10)

#3) 
first_number = input("Enter the first number (13): ")
second_number = input("Enter the second number (9): ")
total_sum = int(first_number) + int(second_number)


#4) 
height_input = input("Enter your height (1.54): ")
height_float = float(height_input)


#5) 
price_input = input("Enter the product price (2.50): ")
result = float(price_input) + 5.5


#6)
name = "ნიკა"      
age = 25            
height = 1.57
print(type name)
print(type age)
print(type height)

#7)
name = input("Enter your name: ")
age_input = input("Enter your age: ")
age = int(age_input)

#8)
num1_input = input("Enter the first number: ")
num2_input = input("Enter the second number: ")
num1 = int(num1_input)
num2 = int(num2_input)

#9)
favorite_number = input("Enter your favorite number (5): ")
result = int(favorite_number) - 3

#10)
age_input = input("Enter your age: ")
age = int(age_input)











