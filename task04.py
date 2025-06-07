num = int(input("butun sonni kiriting: "))
num2 = int(input("Stepni kiriting: "))

if num < 15 :
    for i in range(num, 16,num2):
        print(i)
else:
    print("15dan kichik son kiriting")