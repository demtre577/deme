#1) შექმენი ცვლადი name, შეინახე შენი სახელი და დაბეჭდე მისი მნიშვნელობა და ტიპი.
#2) შექმენი ცვლადი age, შეინახე შენი ასაკი და დაბეჭდე მისი მნიშვნელობა და ტიპი.
#3) მომხმარებელს შეაყვანინე ასაკი  input()-ით, გადააქციე int-ად და დაბეჭდე მისი ტიპი.
#4) მომხმარებელს შეაყვანინე სიმაღლე input-ით, გადააქციე float-ად და დაბეჭდე მისი ტიპი.
#5) მომხმარებელს შეაყვანინე სახელი, ასაკი და სიმაღლე. შემდეგ დაბეჭდე ეს ინფორმაცია f-string-ის გამოყენებით.


#1) 
name="demetre"
print(name)
print(type(name))

#2) 
age=12
print(age)
print(type(age))
      
#3)
age=int(input("enter your age"))
print(type(age))

#4)
hight=float(input("enter your age"))
print(type(age))

#5)
name=input("your name:")
age=int(input("your age :"))
hight=float(input("your hight"))

print(f"name: age: hight")





