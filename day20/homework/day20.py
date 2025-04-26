# 2) დადებითი, უარყოფითი ან ნული + ლუწი/კენტი
number = int(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 3) შეყვანა მანამ სანამ უარყოფითს არ შეიყვანს და ჯამი
total = 0

while True:
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number < 0:
        break
    total += number

print("დადებითი რიცხვების ჯამი არის:", total)

# 4) შეყვანა მანამ სანამ უარყოფითს არ შეიყვანს და ლუწ/კენტი რაოდენობა
even_count = 0
odd_count = 0

while True:
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number < 0:
        break
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("ლუწი რიცხვების რაოდენობა:", even_count)
print("კენტი რიცხვების რაოდენობა:", odd_count)

# 5) 3 მცდელობა PIN კოდის შესაყვანად
correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("შეიყვანეთ PIN კოდი: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts += 1

if attempts == 3:
    print("Access Denied")

# 6) შეყვანა სანამ -1 არ შეიყვანს და საშუალოს გამოთვლა
total = 0
count = 0

while True:
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number == -1:
        break
    total += number
    count += 1

if count > 0:
    average = total / count
    print("საშუალო არის:", average)
else:
    print("არ შეყვანილა არცერთი რიცხვი.")

# 7) წინადადებიდან ხმოვნებისა და თანხმოვნების რაოდენობის დათვლა
sentence = input("შეიყვანეთ წინადადება: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("ხმოვნების რაოდენობა:", vowel_count)
print("თანხმოვნების რაოდენობა:", consonant_count)

# 8) სია და მესამე ელემენტის დაბეჭდვა
fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])  # მესამე ელემენტი არის ინდექსზე 2

# 9) სიის მეორე ელემენტის შეცვლა და დაბეჭდვა
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)

# 10) ინდექსით ფერის ამოღება
colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
index = int(input("შეიყვანეთ ინდექსი (0-დან 4-მდე): "))
print(colors[index])

# 11) ბოლო ელემენტის შეცვლა
animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"
print(animals)

# 12) ინდექსით ფერის შეცვლა სიაში
colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = int(input("შეიყვანეთ ინდექსი (0-დან 3-მდე): "))
new_color = input("შეიყვანეთ ახალი ფერი: ")
colors[index] = new_color
print(colors)
