print("1) USD\n2) UAH\n3) RU")
a = int(input("Виберіть валюту(1-3): "))
b = int(input("Виберіть в яку валюту переводити(1-3): "))
c = int(input("Скільки перевести?: "))
1 > 2 > 3
if 1 <= a <= 3:
    if 1 <= b <= 3:
        if a == b:
            cost = c
        elif a == 3 and b == 2:
            cost = c * 1.25
        elif a == 3 and b == 1:
            cost = c * 1.5
        elif a == 2 and b == 3:
            cost = c * 1.25
        elif a == 2 and b == 1:
            cost = c * 1.25
        elif a == 1 and b == 3:
            cost = c / 1.5
        elif a == 1 and b == 2:
            cost = c / 1.25
    else:
        print("Неправильне число")
else:
    print("Неправильне число")

print(f"Ви взяля {a} щоб перевести в {b} і кількість їхня: {c} це буде дорівнювати: {cost}")
print(a,b,c,)