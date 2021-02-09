with open('file1.txt')as file1:
    raw_data1 = file1.readlines()
    data1 = [data.strip() for data in raw_data1]
    print(data1)

with open('file2.txt')as file2:
    raw_data2 = file2.readlines()
    data2 = [data.strip() for data in raw_data2]
    print(data2)

# Write your code above 👆
result = [item for item in data1 if item in data2]
print(result)


