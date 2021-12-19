Pyramid = int(input("Enter your Pyramid "))
for i in range(Pyramid + 1, 0, -1):
    for j in range(0, i-1):
        print("*", end='')
    print("")
