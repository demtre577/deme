# 1.მომხმარებელს სთხოვე შეიყვანოს თავისი საყვარელი წიგნის დასახელება. დაბეჭდე ეს ტექსტი ჯერ პირველი და ბოლო ასოს გამოყენებით (ინდექსებით).

# 2.შექმენი ცვლადი user_city = "tbilisi". დაბეჭდე ეს ქალაქი ისე, რომ პირველი ასო იყოს დიდი.

# 3.მომხმარებელს სთხოვე შეიყვანოს თავისი საყვარელი ფრაზა. დაბეჭდე ეს შეტყობინება სრულად დიდ ასოებში.

# 4.მოცემულია ტექსტი: text = "learning python is very interesting and rewarding". დაითვალე და დაბეჭდე, რამდენჯერ გვხვდება ასო "e" ამ ტექსტში.

# 5.შექმენი ცვლადი sentence = "I like offline games.". შეცვალე სიტყვა "offline" სიტყვით "online" და დაბეჭდე მიღებული ახალი წინადადება.

# 6.მოცემულია ტექსტი: text = "Welcome to the Python course". იპოვე და დაბეჭდე, მერამდენე ინდექსზე იწყება სიტყვა "Python".

# 7.შექმენი ცვლადი word = "Developer". ამოჭერი და დაბეჭდე ამ სიტყვის პირველი 5 ასო.

# 8.შექმენი ცვლადი promo_code = "SALE2024". გარდაქმენი ეს ტექსტი სრულად პატარა ასოებად და დაბეჭდე შედეგი.


#1)
favorite_book = input("გთხოვთ, შეიყვანოთ თქვენი საყვარელი წიგნის დასახელება: ")
if favorite_book:
    first_letter = favorite_book[0]   # პირველი ასო (ინდექსი 0)
    last_letter = favorite_book[-1]   # ბოლო ასო (ინდექსი -1)
    
    print(f"პირველი ასო: {first_letter}")
    print(f"ბოლო ასო: {last_letter}")
else:
    print("ტექსტი არ არის შეყვანილი.")




#2)
user_city = "tbilisi"

capitalized_city = user_city.capitalize()

print(capitalized_city)



#3)
favorite_phrase = input("გთხოვთ, შეიყვანოთ თქვენი საყვარელი ფრაზა: ")
uppercase_phrase = favorite_phrase.upper()

print(uppercase_phrase)



#4)
text = "learning python is very interesting and rewarding"
e_count = text.count("e")

print(f"ასო 'e' ტექსტში გვხვდება {e_count}-ჯერ.")


#5)
sentence = "I like offline games."
new_sentence = sentence.replace("offline", "online")

print(new_sentence)


#6)
text = "Welcome to the Python course"
index = text.find("Python")

print(f"სიტყვა 'Python' იწყება ინდექსზე: {index}")



#7)
word = "Developer"
first_five_letters = word[0:5]

print(first_five_letters)


#8)
promo_code = "SALE2024"
lowercase_promo = promo_code.lower()

print(lowercase_promo)
























