input_string = input()
list1 = []
list1[:0] = input_string
list2 = []
list3 = []
list2 = set(list1)
print(list2)
for i in list2:
    list3.append(list1.count(i))
print(list3)
list3, list2 = zip(*sorted(zip(list3, list2)))
x = list2[::-1]
y = list3[::-1]
print(list(x))
print(list(y))
    
