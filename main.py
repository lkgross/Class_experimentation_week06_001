mountains = ['Mount Kilimanjaro', 'Mount Kenya', 'Mount Stanley', 'Mount Meru']
heights = [5895, 5199, 5109, 4562]
facts = []
for i in range(len(mountains)):
    facts.append(f'The height of {mountains[i]} is {heights[i]} m.')
print(facts)

mountains[3] = 'Mount Speke'
print(mountains)
print(heights)
print(min(heights))
print(max(heights))
# The total height is not meaningful.
print(sum(heights))
print(round(3.14159, 3))

for height in heights:
    print(height)

print()

for i in range(len(heights)):
    print(heights[i])

print()

print(5 > 3)
print(heights[0] > 4562)

print()

print(type(5.3))
print(type(3))
print(type('Daniel'))

# In computer science True and False are "boolean values",
# known to Python as "bool".
print(type(5 > 3))

print(f"Is 3 > 3? {3 > 3}")
print(f"Is 3 = 3? {3 == 3}")
print(f"Is 3 >= 3? {3 >= 3}")

print(type(True))
print(type('True'))
# Python looks for a variable called TRUE.
# It doesn't find a value for a variable TRUE.
# type(TRUE)

print(f"Is 3 not equal 3? {3 != 3}")

print(heights)
print()

print("Checking whether the mountains are higher than 4562 m.")
for height in heights:
    print("Checking mountain:")
    print(height > 4562)
print("We checked all the mountains.")

print()

print("Checking whether the mountains are higher than 4562 m.")
for i in range(len(mountains)):
    print(f"Checking {mountains[i]}: {heights[i] > 4562}")
print("We checked all the mountains.")

print()

# if 5895 > 4562:
#    print(f"The mountain is higher than 4562 m.")

if 4562 > 4562:
    print(f"The mountain is higher than 4562 m.")

print("Checking whether the mountains are higher than 4562 m.")
for i in range(len(mountains)):
    if heights[i] > 4562:
        print(f"{mountains[i]} is higher than 4562 m.")
print("We checked all the mountains.")

mountain_info = [['Mount Kilimanjaro', 5895], ['Mount Kenya', 5199],
                 ['Mount Stanley', 5109], ['Speke', 4562]]

print(mountain_info[3])
print(mountain_info[3][0])
print(mountain_info[3][1])

mountain_info[3][0] = 'Mount Meru'
print(mountain_info)




