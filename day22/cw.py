# 1) მოცემულია:
# text = "I like JavaScript"

# replace() მეთოდის გამოყენებით შეცვალე "JavaScript" → "Python".

# 2) მომხმარებელს შემოატანინე სიტყვა და გამოიტანე:
# მთლიანად პატარა ასოებით;
# მთლიანად დიდი ასოებით.
# მოცემულია:
# text = "   Hello Python   "

# 3) strip() მეთოდის გამოყენებით მოაშორე ტექსტის დასაწყისში და ბოლოში არსებული ზედმეტი space-ები.

# 4) მოცემულია:
# text = "python is a programming language"

# title() მეთოდის გამოყენებით თითოეული სიტყვის პირველი ასო გახადე დიდი.

# 5) მოცემულია:
# words = ["Python", "is", "easy"]

# join() მეთოდის გამოყენებით მიიღე:

# Python is easy

# 6) მოცემულია:
# words = ["2026", "09", "11"]

# join() მეთოდის გამოყენებით მიიღე:

# 2026-09-11

# 7) მოცემულია:
# text = "Python"

# slicing-ის გამოყენებით გამოიტანე პირველი 3 სიმბოლო:
# Pyt

# 8) მოცემულია:
# text = "Programming"

# slicing-ის გამოყენებით გამოიტანე ბოლო 3 სიმბოლო.




 #1)
text = "I like JavaScript"

new_text = text.replace("JavaScript", "Python")

print(new_text)


#2)
user_word = input("შემოიტანეთ ნებისმიერი სიტყვა: ")

print("მთლიანად პატარა:", user_word.lower())
print("მთლიანად დიდი:", user_word.upper())



#3)
text = "   Hello Python   "
clean_text = text.strip()
print(f"ორიგინალი: '{text}'")
print(f"გასუფთავებული: '{clean_text}'") 


#4)
text = "python is a programming language"
title_text = text.title()
print(title_text)


#5)
words = ["Python", "is", "easy"]
result = " ".join(words)
print(result)



#6)
words = ["2026", "09", "11"]
date_result = "-".join(words)
print(date_result)


#7)
text = "Python"
first_three = text[0:3]  
print(first_three)


#8)
text = "Programming"
last_three = text[-3:]
print(last_three)