"""
range(comienzo, fin, pasos)
"""

my_range =  range(1,5)
type(my_range)

for i in my_range:
    print(i)

my_range1 =  range(0,7, 2)

my_range2 =  range(0,8, 2)

print("== " + str(my_range1 == my_range2))

for i in my_range1:
    print(f"range(0, 7, 2)= {i}")

for i in my_range2:
    print(f"range(0, 8, 2)= {i}")


print(f"id my_range1 {id(my_range1)}")
print(f"id my_range2 {id(my_range2)}")

print("is " + str(my_range1 is my_range2))

for i in range(0, 51, 2):
    if i != 0:
        print("PARES: " + str(i))