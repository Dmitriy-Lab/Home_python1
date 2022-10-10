# Напишите программу, которая на вход принимает число (N), 
# а на выходе показывает все чётные числа от 1 до N

number = int(input("Введите число N: ")) 

if number > 1:
    count = 2
    while count <= number:
        print(count)
        count +=2
elif number < 1:
    count = 0
    while count >= number:
        print(count)
        count -=2   
elif number == 1:
    print("Нет таких чисел")