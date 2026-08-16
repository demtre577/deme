# 1) გამოიტანე რიცხვები 1-დან 20-მდე, მხოლოდ ლუწები.
# 2) გამოიტანე რიცხვები 5-დან 50-მდე, რომლებიც იყოფა 5-ზე.
# 3) მომხმარებელს შემოატანინე რიცხვი და for loop-ის გამოყენებით გამოიტანე 1-დან ამ რიცხვამდე ყველა რიცხვი.
# 4) მომხმარებელს შემოატანინე რიცხვი და გამოიტანე მისი გამრავლების ტაბულა 1-დან 10-მდე.
# 5) იპოვე რიცხვების 1-დან 100-მდე ჯამი


#1)
for number in range(2, 18):
    if number % 2 == 0:
        print(number)

#2)
for number in range(50, 4, -5):
    print(number)

#3)
user_input = int(input("შემოიტანეთ რიცხვი: "))
for number in range(1, user_input + 1):
    print(number)

#4)
number = int(input("შემოიტანეთ რიცხვი: "))

print(f"\n{number}-ის გამრავლების ტაბულა:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

#5)
total_sum = 0

for number in range(1, 101):
    total_sum += number

print("ჯამი არის:", total_sum)








