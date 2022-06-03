
str = input("Enter a string consisting of only the digits 0 or 1: ")

terminated = False
for digit in str:
    if digit != "0" and digit != "1":
        terminated = True
        break

if not terminated:
    for index in range(len(str)+1):
        if index == 0:
            start = str[index]
            count = 1
        elif index == len(str):
            print(count, str[index-1] + "'s")

        elif str[index] == str[index-1]:
            count += 1
        elif str[index] != str[index-1]:
            print(count, str[index-1] + "'s")
            start = str[index]
            count = 1


