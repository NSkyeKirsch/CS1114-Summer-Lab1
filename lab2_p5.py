start = int(input("What is the starting length of the triangle? "))
end = int(input("What is the ending length of the triangle? "))

for row in range(start, end+1):
    print(str(row)*row)