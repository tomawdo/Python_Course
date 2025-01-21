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
'''

x = {(1, 2): 1, (2,3):2}
print(x[1, 2])



