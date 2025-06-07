num = input("7 ta sonni vergul bilan kiriting: ")
b = num.strip().split(",")

if len(b) == 7:
    b = list(map(int, b)) 
    min_value = b[0]

    for i in b:
        if i < min_value:
            min_value = i

    print(min_value)
else:
    print("Iltimos, aniq 7 ta son kiriting.")

    #bu misolda listlardan foydalanmasak chiqara olmadim