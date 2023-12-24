import math

def find_min_max():
    try:
        # Введення трьох чисел
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # Знаходження найменшого числа з використанням операторів if
        if num1 <= num2 and num1 <= num3:
            min_num = num1
        elif num2 <= num1 and num2 <= num3:
            min_num = num2
        else:
            min_num = num3

        # Знаходження найбільшого числа з використанням операторів if
        if num1 >= num2 and num1 >= num3:
            max_num = num1
        elif num2 >= num1 and num2 >= num3:
            max_num = num2
        else:
            max_num = num3

        # Виведення результатів
        print("The smallest number is:", min_num)
        print("The largest number is:", max_num)

    except ValueError:
        print("ERROR: Please enter valid numeric values.")

def points_in_yellow_region():
    try:
        # Введення кількості точок
        n = int(input("Enter the number of points: "))
        
        # Ініціалізація лічильника точок, що потрапляють в геометричну область
        count = 0
        
        # Зчитування координат точок та перевірка, чи вони потрапляють в область
        for i in range(1, n + 1):
            x = float(input(f"Enter the x-coordinate of point {i}: "))
            y = float(input(f"Enter the y-coordinate of point {i}: "))
            
            # Перевірка, чи точка потрапляє в жовту геометричну область
            if x <= 0 and y <= -1 and y >= -x:
                count += 1
        
        # Виведення результату
        print(f"The number of points in the yellow region is: {count}")

    except ValueError:
        print("ERROR: Please enter valid numeric values.")

def calculate_un(n):
    return (math.factorial(n) - 3**n) / (n**n)

def check_convergence():
    e = 1e-5  # мала величина для переривання циклу обчислення суми сходиться ряду
    g = 1e2   # величина для переривання циклу обчислення суми розходиться ряду

    n = 1
    while True:
        ratio = calculate_un(n+1) / calculate_un(n)
        if abs(ratio) < e or abs(ratio) > g:
            break
        n += 1

    return n