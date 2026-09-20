# 1) მომხმარებელს სთხოვე შეიყვანოს თავისი სახელი და გვარი. დაბეჭდე შეყვანილი ტექსტი ჯერ სრულად დიდ ასოებით, ხოლო შემდეგ 
# სრულად პატარა ასოებით.

# 2) შექმენი ცვლადი, რომელშიც შეინახავ ტექსტს პატარა ასოებით: "python is cool". დაბეჭდე ეს ტექსტი ეკრანზე ისე, რომ მხოლოდ
# პირველი ასო იყოს დიდი, ხოლო დანარჩენი — პატარა.

# 3) შექმენი ცვლადი: sentence = "I love cats, cats are my favorite animal.". შეცვალე ტექსტში არსებული ყველა სიტყვა "cats"
# სიტყვით "dog" და დაბეჭდე მიღებული ახალი წინადადება.

# 4) მოცემულია ტექსტი: text = "Python is the best programming language". იპოვე და დაბეჭდე, მერამდენე პოზიციაზე (ინდექსზე)
# იწყება სიტყვა "best". ასევე შეამოწმე, რას დააბრუნებს პროგრამა, თუ მოძებნი სიტყვას "JavaScript".

# 5) შექმენი ცვლადი:
# text = "Banana, Apple, Banana, Orange, Banana". დაითვალე და დაბეჭდე, რამდენჯერ გვხვდება სიტყვა "Banana" ამ ტექსტში.


#1)
full_name = input("გთხოვთ, შეიყვანოთ თქვენი სახელი და გვარი: ")
print(full_name.upper())
print(full_name.lower())

#2)
text = "python is cool"
print(text.capitalize())


#3)
text = "python is cool"
print(text.capitalize())

#4)
text = "Python is the best programming language"
print(text.find("best"))
print(text.find("JavaScript"))


#5)
text = "Banana, Apple, Banana, Orange, Banana"
print(text.count("Banana")) 





















