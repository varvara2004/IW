import math

def calculate_sum(n):
    total_sum = 0
    
    for i in range(1, n + 1):
        total_sum += 1 / math.sin(i)
    
    return total_sum

n = int(input("Введите натуральное число n: "))
c = calculate_sum(n)
print(f"Результат: {c}")




import math

def calculate_expression1(x, n):
    result = 1
    for i in range(1, n+1):
        result *= (x - i*n)
    return result

def calculate_expression2(x, n):
    result = 0
    for i in range(1, n+1):
        temp = 1
        for j in range(i+1):
            temp *= (x + j)
        result += 1/temp
    return result

def calculate_expression3(x, n):
    result = 0
    for i in range(1, n+1):
        result += (x**i) / math.factorial(i)
    return result

x = float(input("Введите значение x: "))
n = int(input("Введите значение n: "))

print("Результат выражения x(x-n)(x-2n)(x-3n)…(x-n**2) равен:", calculate_expression1(x, n))
print("Результат выражения 1/x + 1/x(x+1) + … + 1/x(x+1)…(x +n) равен:", calculate_expression2(x, n))
print("Результат выражения x^1/1! + x^2/2! + x^3/3! + … x**n/n! равен:", calculate_expression3(x, n))
