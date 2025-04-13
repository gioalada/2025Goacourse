
print("2) for ციკლი:")
for i in range(0, 21):
    if i % 2 == 0:
        print("even -", i)
    else:
        print("odd -", i)

print("\n")  

print("3) while ციკლი:")
i = 0
while i <= 20:
    if i % 2 == 0:
        print("even -", i)
    else:
        print("odd -", i)
    i += 1

print("\n")

print("4) სახელის შემოწმება:")
my_name = "გიო"  
user_name = input("შეიყვანე შენი სახელი: ")

if user_name == my_name:
    print("coincidence")
else:
    print("სხვადასხვა სახელები გვაქვს")

print("\n")


print("8) ქულის შემოწმება:")
score = int(input("შეიყვანე გამოცდის ქულა: "))

if score > 70:
    print("passed")
else:
    print("failed")

print("\n")

# 6) ქულის მიხედვით შეფასება (grade)
print("6) grade შეფასება:")
score = int(input("კიდევ ერთხელ შეიყვანე ქულა grade-ისთვის: "))

if score > 70:
    print("შენი grade არის: გ")
elif score > 69:
    print("შენი grade არის: პ")
elif score > 47:
    print("შენი grade არის: ო")
elif score > 26:
    print("შენი grade არის: ი")
else:
    print("შენი grade არის: უ")
