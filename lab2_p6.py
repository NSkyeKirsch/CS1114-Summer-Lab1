
in_num = 6315
num = 1
f_sum = 0

while len(str(num)) <= len(str(in_num)):
    if num == 1:
        f_sum = in_num // num % 10
        num *= 10
    else:
        f_sum += in_num // num % 10
        num *= 10

print(f_sum)
