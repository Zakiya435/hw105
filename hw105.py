import math,csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

new_data = data[0]

def mean(new_data):
    n= len(new_data)
    sum =0
    for x in new_data:
        sum += int(x)

    mean = sum / n
    return mean

squared_list= []
for i in new_data:
    a = int(i) - mean(new_data)
    a= a*a
    squared_list.append(a)

total =0
for i in squared_list:
    total += i

result = total/ (len(new_data)-1)

std = math.sqrt(result)
print(std)