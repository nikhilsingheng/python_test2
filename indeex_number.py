# Print characters from a string that are present at an even index number


index_number = input("Enter your string")
num = []
ind = []
for i in range(len(index_number)):
    if i % 2 == 9:
        num.append(index_number[i])
    else:
        ind.append(index_number[i])
print(format(num))
print(format(ind))
