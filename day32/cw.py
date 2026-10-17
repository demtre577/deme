# 1) შექმენი Tuple სახელად `numbers`, რომელშიც იქნება 6 რიცხვი. გამოიყენე `len()` ფუნქცია ელემენტების რაოდენობის გასაგებად და `in`
# ოპერატორით შეამოწმე, არის თუ არა რიცხვი `30` Tuple-ში.

# 2) შექმენი Set სახელად `fruits`, რომელშიც იქნება 5 ხილი. `add()` მეთოდით დაამატე ახალი ხილი, `discard()` მეთოდით წაშალე 
# ერთ-ერთი ხილი და დაბეჭდე მიღებული Set.

# 3) შექმენი Tuple სახელად `animals`, რომელშიც იქნება 5 ცხოველი. `in` ოპერატორით შეამოწმე, არის თუ არა `"lion"` Tuple-ში, 
# შემდეგ კი `len()` ფუნქციით დაბეჭდე Tuple-ის სიგრძე.

# 4) შექმენი Set სახელად `numbers`, რომელშიც იქნება 6 განსხვავებული რიცხვი. `remove()` მეთოდით წაშალე ერთი რიცხვი, `add()`
#  მეთოდით დაამატე ახალი რიცხვი და `in` ოპერატორით შეამოწმე, არის თუ არა ახალი რიცხვი Set-ში.

# 5) შექმენი Set სახელად `languages`, რომელშიც იქნება 4 პროგრამირების ენა. `len()` ფუნქციით გაიგე ელემენტების რაოდენობა,
# `discard()` მეთოდით სცადე ისეთი 
# ენის წაშლა, რომელიც Set-ში არ არსებობს, ხოლო `in` ოპერატორით შეამოწმე, არის თუ არა `"Python"` Set-ში. ბოლოს დაბეჭდე Set


#1)
numbers = (10, 20, 30, 40, 50, 60)
length = len(numbers)
print(f"Number of elements: {length}")
if 30 in numbers:
    print("The number 30 is in the Tuple!")
else:
    print("The number 30 is not in the Tuple!")


#5)
languages = {"Python", "JavaScript", "C++", "Java"}
print(len(languages))  
languages.discard("Ruby") 
print("Python" in languages)  
print(languages)



#2)
fruits = {"apple", "banana", "cherry", "orange", "mango"}
fruits.add("grape")
fruits.discard("banana")
print(fruits)



#3)
animals = ("lion", "tiger", "elephant", "bear", "wolf")

if "lion" in animals:
    print("Yes, 'lion' is in the Tuple!")
else:
    print("No, 'lion' is not in the Tuple!")

print(f"Length of the Tuple: {len(animals)}")



#4)
numbers = {10, 20, 30, 40, 50, 60}
numbers.remove(30)
numbers.add(70)
print(70 in numbers)  






