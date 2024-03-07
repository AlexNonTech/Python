# foods = list()
# while True:
#     food = input("What food do you like?: ").lower()
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
print(foods)
