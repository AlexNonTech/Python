store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]


to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1] / 0.82)

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store_euros))

for i in store_euros:
    print(i)

print("\n")

for i in store_dollars:
    print(i)
