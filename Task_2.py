
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#  Он называет сумму этих чисел S и их произведение P. 
#  Помогите Кате отгадать задуманные Петей числа.

print("Привет, Катя, гений математики!")

x = 1
y = 3
s = x + y
p = x * y
print(f"Я загадал 2 натуральных числа, X и Y. X,Y ≤ 1000. Cумма загаданных чисел: {s}, а их произведение: {p}. Отгадай, что за числа я загадал. Петя.")

running = True

while running:
    x1 = int(input("Введите число X: "))
    y1 = int(input("Введите число Y: "))
    
    if x == x1 and y == y1:
        print("Верно! Ты угадала оба числа!")
        running = False
    elif x != x1 and y != y1:
        print("Не угадала оба числа. Попробуй ещё!")
    elif x != x1 :
        print("Ты угадала Y, но не угадала X... Подумай ещё!")
    elif y != y1:
        print(f"X угадала! Это {x}. А Y? Сумма загаданных чисел: {s}, а их произведение: {p}.")
       

