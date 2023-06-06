a = int(input())
b = input()

b_third = int(b[2])
b_second = int(b[1])
b_first = int(b[0])

b_third_res = a * b_third
b_second_res = a * (int(b[1]) * 10)
b_first_res = a * (int(b[0]) * 100)

print(a * b_third)
print(a * b_second)
print(a * b_first)
print(b_first_res + b_second_res + b_third_res)