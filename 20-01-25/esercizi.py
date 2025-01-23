'''
data1 = 'a', 'b'
data2 = ('a', 'b')
print(data1 == data2)

#72
l1 = [1,2,3]

for v in range(len(l1)):
    l1.insert(1, l1[v])
print(l1)


box = {"biscuits": 2, "cake": 2}
crates = {}
crates["box"] = box
print(len(crates["box"]))


x = {(1, 2): 1, (2,3):2}
print(x[1, 2])
'''

# 68
box = {}
jars = {}
crates = {}

box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4

crates[ 'box'] = box
crates['jars'] = jars

print(len(crates[box]))

#77 - C
num = [1,2,3]
val = num
del val[:]
print(num, val)

#78 - D
data = {}
data[1] = 1
data['1'] = 2
data[1.0] = 4

res = 0
for d in data:
    res += data[d]

print(res)

#108
x = 1
print(---1)

#112
res = str(bool(1) + float(12) / float(2))
print(res)

#113
print("Mike" > "Mikey")

#152
x = '\''
print(len(x))