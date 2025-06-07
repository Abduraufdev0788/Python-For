num = input("7 ta sonni vergul bilan kiriting: ")
b = num.strip().split(",")

if len(b) == 7:
    b = list(map(int, b)) 
    max_value = b[0]

    for i in b:
        if i > max_value:
            max_value = i

    print(max_value)
else:
    print("Iltimos, aniq 7 ta son kiriting.")
#bunda ham listlardan foydalanamiz ekan