num = input("Sonlarni kiriting (vergul bilan): ")
b = num.split(",")
b = list(map(int, b))

min_val = b[0]
max_val = b[0]

for i in b:
    if i < min_val:
        min_val = i

for y in b:
    if y > max_val:
        max_val = y

norm_value = (min_val + max_val) / 2
print(norm_value)
