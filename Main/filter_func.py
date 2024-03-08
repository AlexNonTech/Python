

friends = [("Lauren", 18),
           ("Paul", 20),
           ("Suzy", 16),
           ("Mike", 17)]

age = lambda data:data[1] >= 18

enough_old = list(filter(age, friends))

for i in enough_old:
    print(i)
